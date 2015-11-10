from tracking.models import Transaction


def run():
    Transaction.objects.transact_rate_balance()
