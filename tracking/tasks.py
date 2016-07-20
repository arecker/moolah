from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.utils import timezone

from models import Transaction, Rate, Allowance


def today():
    return timezone.now().strftime('%m/%d/%Y')


@periodic_task(run_every=(crontab(minute=0, hour=0)), name="compute-rate", ignore_result=True)
def compute_rate():
    balance = Rate.objects.all().total()
    description = 'Rate Balance for {}'.format(today())
    Transaction.objects.create(description=description, amount=balance)


@periodic_task(run_every=(crontab(0, 0, day_of_month='1')), name="compute-allowance", ignore_result=True)
def compute_allowance():
    for allowance in Allowance.objects.all():
        Transaction.objects.create(
            description='Allowance for {}'.format(today()),
            amount=allowance.amount,
            allowance=allowance
        )
