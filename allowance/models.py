from django.db import models
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


def get_month():
    return timezone.now().month


def get_year():
    return timezone.now().year


class Period(models.Model):
    month = models.IntegerField(default=get_month, choices=month_choices)
    year = models.BigIntegerField(default=get_year)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', '-month']
    
    def __unicode__(self):
        return '{0} {1}'.format(month, year)
