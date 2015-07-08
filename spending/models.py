from django.db import models
from django.utils import timezone
import uuid


def _get_month():
    return timezone.now().month


def _get_year():
    return timezone.now().year


class MonthlyPeriod(models.Model):
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

    class Meta:
        ordering = ['-year', '-month']
        unique_together = ('month', 'year')
