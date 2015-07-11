from spending.models import Budget, Transaction, Period
from django.contrib.auth.models import User


def run(*args):
    """
    re opens a new period for all
    budgets and calculates allowance
    """
    import ipdb
    ipdb.set_trace()
    REOCCUR = parse_args(args)
    if REOCCUR not in [0, 1]:
        print('No reoccurance specified')
        exit(1)

    # Close old period
    old_period = Period.objects.filter(reoccuring=REOCCUR).latest()
    old_period.closed = True
    old_period.save()

    # Open new period
    new_period = Period()
    new_period.reoccuring = REOCCUR
    new_period.save()

    for b in Budget.objects.filter(reoccuring=REOCCUR):
        if b.shared:
            balance = Transaction.objects.filter(
                period=old_period,
                budget=b
            ).balance()
            transact_allowance(balance, new_period, b)
        else:
            for u in User.objects.all():
                balance = Transaction.objects.filter(
                    period=old_period,
                    budget=b,
                    user=u
                ).balance()
                transact_allowance(balance, new_period, b, user=u)


def parse_args(args):
    if 'weekly' in args:
        return 0
    elif 'monthly' in args:
        return 1
    else:
        return None


def transact_allowance(balance, period, budget, user=None):
    opening = Transaction()
    opening.reason = 1
    opening.period = period
    opening.budget = budget
    opening.negative = balance < 0
    opening.amount = abs(balance)
    opening.description = 'Allowance for {0}'.format(period)
    opening.user = user
    opening.save()
