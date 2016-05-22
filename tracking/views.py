from rest_framework import viewsets

from models import Allowance, Transaction
from serializers import TransactionSerializer, AllowanceTransactionSerializer


transactions = Transaction.objects


class TransactionViewSet(viewsets.ModelViewSet):
    '''
    Transactions not associated with an allowance
    '''
    queryset = Transaction.objects.without_allowance()
    serializer_class = TransactionSerializer


class AllowanceTransactionViewSet(viewsets.ModelViewSet):
    '''
    Transactions associated with the current user's allowance
    '''
    queryset = Transaction.objects.with_allowance()
    serializer_class = AllowanceTransactionSerializer

    def get_queryset(self, *args, **kwargs):
        allowance = Allowance.objects.get(user=self.request.user)
        qs = super(AllowanceTransactionViewSet, self).get_queryset(*args, **kwargs)
        return qs.filter(allowance=allowance)
