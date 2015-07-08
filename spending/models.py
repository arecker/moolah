from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid


class TransactionBaseQueryset(models.query.QuerySet):
    def balance(self):
        positive = (self.filter(
            negative=False).aggregate(
                models.Sum('amount'))['amount__sum'] or 0)
        negative = -1 * (self.filter(
            negative=True).aggregate(
                models.Sum('amount'))['amount__sum'] or 0)
        return positive + negative


class TransactionBase(models.Model):
    reason_choices = [
        (0, 'Allowance'),
        (1, 'Purchase'),
        (2, 'Refund'),
        (3, 'Penalty'),
        (4, 'Reward'),
        (5, 'Adjustment'),
        (6, 'Error'),
        (7, 'Other')
    ]
    objects = TransactionBaseQueryset.as_manager()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    reason = models.IntegerField(choices=reason_choices, default=1)
    negative = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=120, null=True, blank=True)
    memo = models.TextField(null=True, blank=True)

    class Meta:
        abstract = True


def _get_month():
    return timezone.now().month


def _get_year():
    return timezone.now().year


class PeriodBase(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    timestamp = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)

    class Meta:
        abstract = True


class MonthlyPeriodManager(models.Manager):
    pass


class MonthlyPeriod(PeriodBase):
    objects = MonthlyPeriodManager()
    month_choices = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    )

    month = models.IntegerField(default=_get_month, choices=month_choices)
    year = models.BigIntegerField(default=_get_year)
    date = models.DateTimeField(blank=True, null=True, editable=False)

    @property
    def display_name(self):
        return '{0} {1}'.format(
            dict(self.month_choices)[self.month],
            self.year
        )

    def __unicode__(self):
        return self.display_name

    def save(self, *args, **kwargs):
        self.date = timezone.datetime(
            year=self.year,
            month=self.month,
            day=1
        )
        super(MonthlyPeriod, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-year', '-month']
        get_latest_by = 'date'
        unique_together = ('month', 'year')


class MonthlyTransaction(TransactionBase):
    period = models.ForeignKey(MonthlyPeriod)
