from uuid import uuid4
from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator

from moolah.models import TransactionBase
from moolah.utils import to_decimal, get_timestamp


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


class Transaction(TransactionBase):
    pass


def transact_rate_balance():
    transaction = Transaction()
    transaction.description = ('Rate Balance for {0}'
                               .format(get_timestamp()
                                       .strftime("%m/%d/%Y")))
    transaction.amount = Rate.objects.total()
    transaction.save()
