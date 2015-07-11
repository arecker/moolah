from spending.models import Budget, Transaction, Period
from django.contrib.auth.models import User
from decimal import Decimal


def run(*args):
    """
    re opens a new period for all
    budgets and calculates allowance
    """
    REOCCUR = parse_args(args)
    if REOCCUR not in [0, 1]:
        print('No reoccurance specified')
        exit(1)

    # Close old period
    try:
        old_period = Period.objects.filter(reoccuring=REOCCUR).latest()
        old_period.closed = True
        old_period.save()
    except Period.DoesNotExist:
        old_period = None

    # Open new period
    new_period = Period()
    new_period.reoccuring = REOCCUR
    new_period.save()

    for b in Budget.objects.filter(reoccuring=REOCCUR):
        if b.shared:
            if old_period:
                balance = Transaction.objects.filter(
                    period=old_period,
                    budget=b
                ).balance()
            else:
                balance = Decimal(0)
            transact_allowance(balance, new_period, b)
        else:
            for u in User.objects.all():
                if old_period:
                    balance = Transaction.objects.filter(
                        period=old_period,
                        budget=b,
                        user=u
                    ).balance()
                else:
                    balance = Decimal(0)
                transact_allowance(balance, new_period, b, user=u)


def parse_args(args):
    if 'weekly' in args:
        return 0
    elif 'monthly' in args:
        return 1
    else:
        return None


def transact_allowance(balance, period, budget, user=None):
    total = budget.allowance + balance
    opening = Transaction()
    opening.reason = 0
    opening.period = period
    opening.budget = budget
    opening.negative = total < 0
    opening.amount = abs(total)
    opening.description = 'Allowance for {0}'.format(period.display)
    opening.user = user
    opening.save()
