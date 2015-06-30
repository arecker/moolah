"""
1. Open new month
2. Award each user calculated balance
"""
from allowance.models import Transaction, Period
from django.contrib.auth.models import User
from decimal import Decimal
from django.conf import settings
from django.utils import timezone


def run():
    current_period = Period.objects.latest()
    Period().save()
    next_period = Period.objects.latest()
    for user in User.objects.all():
        try:
            balance = Transaction.objects.balance(user=user, period=current_period)
        except:
            balance = Decimal(0)
        adjustment = Decimal(settings.ALLOWANCE_LIMIT) + balance
        Transaction(
            period=next_period,
            user=user,
            reason=0,
            description='{0} {1} monthly allowance'.format(timezone.now().strftime("%B"), next_period.year),
            negative='-' in str(adjustment),
            amount=abs(adjustment)
        ).save()
        
