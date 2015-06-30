from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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

negative_choices = (
    (False, 'plus'),
    (True, 'minus')
)


def get_month():
    return timezone.now().month


def get_year():
    return timezone.now().year


class PeriodManager(models.Manager):
    def latest(self):
        return super(models.Manager, self).order_by('-year', '-month').first()


class Period(models.Model):
    month = models.IntegerField(default=get_month, choices=month_choices)
    year = models.BigIntegerField(default=get_year)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PeriodManager()

    class Meta:
        ordering = ['-year', '-month']
        
    
    def __unicode__(self):
        return '{0}/{1}'.format(self.month, self.year)


class TransactionManager(models.Manager):
    def latest_set_for_user(self, user):
        period = Period.objects.latest()
        return super(models.Manager, self).filter(period=period).filter(user=user)

    
class Transaction(models.Model):
    period = models.ForeignKey(Period)
    user = models.ForeignKey(User)
    negative = models.BooleanField(verbose_name='Sign', choices=negative_choices, default=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=120, null=True, blank=True)
    memo = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TransactionManager()
    
    class Meta:
        ordering = ['timestamp']

    def __unicode__(self):
        if self.negative:
            sign = '-'
        else:
            sign = '+'
        return '{0}{1} {2}'.format(sign, self.amount, self.description)
