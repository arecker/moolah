from uuid import uuid4
from datetime import timedelta, datetime

from django.db import models
from dateutil import parser

from moolah.utils import to_decimal, get_timestamp


def sanitize_dates(func):
    '''
    attempt to convert stringy dates
    to real dates
    '''
    def wrapper(self, *args):
        clean_args = []
        for arg in args:
            if type(arg) is not datetime:
                try:
                    parsed_date = parser.parse(arg.replace('"', ''))
                    zoned_date = get_timestamp(parsed_date)
                    clean_args.append(zoned_date)
                except ValueError:
                    pass
            else:
                clean_args.append(arg)
        return func(self, *clean_args)
    return wrapper


class TransactionBaseQuerySet(models.QuerySet):
    def total(self):
        return self.aggregate(
            models.Sum('amount'))['amount__sum'] or 0

    @sanitize_dates
    def date(self, date):
        return self.filter(timestamp__month=date.month,
                           timestamp__day=date.day,
                           timestamp__year=date.year)

    @sanitize_dates
    def date_range(self, start, end):
        return self.filter(timestamp__lt=end,
                           timestamp__gt=start)

    def today(self):
        return self.date(get_timestamp())

    def days_ago(self, n):
        return self._from_today(n)

    def this_month(self):
        date = get_timestamp()
        return self.filter(timestamp__month=date.month,
                           timestamp__year=date.year)

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


class TransactionBase(models.Model):
    objects = TransactionBaseQuerySet.as_manager()

    id = models.UUIDField(primary_key=True,
                          editable=False,
                          default=uuid4,
                          unique=True)

    description = models.CharField(max_length=120)
    timestamp = models.DateTimeField(default=get_timestamp)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __unicode__(self):
        return '{0} ({1})'.format(self.description,
                                  to_decimal(self.amount))

    class Meta:
        ordering = ['-timestamp']
        abstract = True
