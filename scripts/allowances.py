from enjoying.models import Allowance


def run():
    Allowance.objects.open_period()
