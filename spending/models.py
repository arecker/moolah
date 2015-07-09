from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
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


class BudgetBase(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    allowance = models.DecimalField(max_digits=6, decimal_places=2)
    shared = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('budget_detail', args=[str(self.id)])

    def __unicode__(self):
        return '{0} ({1})'.format(self.name, str(self.allowance))

    class Meta:
        abstract = True


class MonthlyPeriod(PeriodBase):
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


class MonthlyBudget(BudgetBase):
    pass


class MonthlyTransactionQuerySet(TransactionBaseQueryset):
    def latest_period(self, budget=None):
        qs = self.filter(period=MonthlyPeriod.objects.latest())
        if not budget:
            return qs
        return qs.filter(budget=budget)


class MonthlyTransaction(TransactionBase):
    objects = MonthlyTransactionQuerySet.as_manager()
    period = models.ForeignKey(MonthlyPeriod)
    budget = models.ForeignKey(MonthlyBudget)
