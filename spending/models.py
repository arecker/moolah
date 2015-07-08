from django.db import models
from django.utils import timezone
import uuid


def _get_month():
    return timezone.now().month


def _get_year():
    return timezone.now().year


class MonthlyPeriodManager(models.Manager):
    pass


class MonthlyPeriod(models.Model):
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

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    month = models.IntegerField(default=_get_month, choices=month_choices)
    year = models.BigIntegerField(default=_get_year)
    timestamp = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
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
