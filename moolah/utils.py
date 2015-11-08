from decimal import Decimal

from django.utils import timezone

def get_timestamp(time=None):
    time = time or timezone.now()
    return timezone.localtime(time)


def to_decimal(amount, place='0.01'):
    return Decimal(amount).quantize(Decimal(place))
