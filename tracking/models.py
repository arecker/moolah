from uuid import uuid4
from decimal import Decimal
from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


def get_timestamp():
    return timezone.localtime(timezone.now())


def to_decimal(amount, place='0.01'):  # TODO: centralize this
    return Decimal(amount).quantize(Decimal(place))  # with '$'


class RateQuerySet(models.QuerySet):
    def total(self):
        return self.aggregate(
            models.Sum('amount_per_day'))['amount_per_day__sum']


class Rate(models.Model):
    objects = RateQuerySet.as_manager()

    id = models.UUIDField(primary_key=True,
                          editable=False,
                          default=uuid4,
                          unique=True)

    description = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    days = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    amount_per_day = models.DecimalField(max_digits=8,
                                         decimal_places=3,
                                         editable=False,
                                         blank=True)

    def save(self, *args, **kwargs):
        self.amount_per_day = self.amount / Decimal(self.days)
        return super(Rate, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{0} ({1})'.format(self.description,
                                  to_decimal(self.amount_per_day))


class TransactionQuerySet(models.QuerySet):
    def total(self):
        return self.aggregate(
            models.Sum('amount'))['amount__sum']

    def date(self, date):
        return self.filter(timestamp__month=date.month,
                           timestamp__day=date.day,
                           timestamp__year=date.year)

    def date_range(self, start, end):
        return self.filter(timestamp__lt=end,
                           timestamp__gt=start)

    def today(self):
        return self.date(get_timestamp())

    def last_week(self):
        return self._from_today(7)

    def last_month(self):
        return self._from_today(30)

    def last_year(self):
        return self._from_today(365)

    def _from_today(self, days):
        today = get_timestamp()
        start = today - timedelta(days=days)
        return self.date_range(start, today)


class Transaction(models.Model):
    objects = TransactionQuerySet.as_manager()

    id = models.UUIDField(primary_key=True,
                          editable=False,
                          default=uuid4,
                          unique=True)

    description = models.CharField(max_length=120)
    timestamp = models.DateTimeField(default=get_timestamp,
                                     editable=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return '{0} ({1})'.format(self.description,
                                  to_decimal(self.amount))

    class Meta:
        ordering = ['-timestamp']


def transact_rate_balance():
    transaction = Transaction()
    transaction.description = ('Rate Balance for {0}'
                               .format(get_timestamp()
                                       .strftime("%m/%d/%Y")))
    transaction.amount = Rate.objects.total()
    transaction.save()
