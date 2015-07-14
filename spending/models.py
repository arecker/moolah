from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
import calendar
import uuid


reocurring_options = (
    (0, 'Weekly'),
    (1, 'Monthly')
)


class Budget(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    allowance = models.DecimalField(max_digits=6, decimal_places=2)
    shared = models.BooleanField(default=False)
    reoccuring = models.IntegerField(choices=reocurring_options)

    def get_absolute_url(self):
        return reverse('budget_detail', args=[str(self.id)])

    def __unicode__(self):
        return '{0} ({1})'.format(self.name, str(self.allowance))


class Period(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    timestamp = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    start = models.DateField(default=timezone.now)
    end = models.DateField(blank=True, null=True)
    reoccuring = models.IntegerField(choices=reocurring_options)

    def save(self, *args, **kwargs):
        """
        automatically populate 'stop'
        """
        if self.reoccuring is 0:
            self.end = self.start + timezone.timedelta(days=6)
        elif self.reoccuring is 1:
            self.end = self.start + timezone.timedelta(
                days=(
                    calendar.monthrange(
                        self.start.year,
                        self.start.month
                    )[1] - 1
                )
            )
        super(Period, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.display

    @property
    def display(self):
        return '{0} to {1}'.format(
            self.start.strftime("%m/%d"),
            self.end.strftime("%m/%d")
        )

    class Meta:
        ordering = ['-start', ]
        get_latest_by = 'start'


class TransactionQueryset(models.query.QuerySet):
    def balance(self):
        positive = (self.filter(
            negative=False).aggregate(
                models.Sum('amount'))['amount__sum'] or 0)
        negative = -1 * (self.filter(
            negative=True).aggregate(
                models.Sum('amount'))['amount__sum'] or 0)
        return positive + negative

    def latest_period(self, budget):
        return self.filter(
            budget=budget
        ).filter(
            period=Period.objects.filter(
                reoccuring=budget.reoccuring
            ).latest()
        )


class Transaction(models.Model):
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
    objects = TransactionQueryset.as_manager()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True)
    reason = models.IntegerField(choices=reason_choices, default=1)
    negative = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=120, null=True, blank=True)
    memo = models.TextField(null=True, blank=True)
    period = models.ForeignKey(Period)
    budget = models.ForeignKey(Budget)

    def __unicode__(self):
        return self.display

    def get_absolute_url(self):
        return reverse('transaction_detail', args=[str(self.id)])

    @property
    def display(self):
        return '{0} ({1})'.format(self.description, self.pretty_amount)

    @property
    def pretty_amount(self):
        sign = ''
        if self.negative:
            sign = '- '
        return '{0}${1}'.format(sign, self.amount)

    @property
    def logged_by(self):
        return self.user or 'Automatic'
