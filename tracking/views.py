from rest_framework import viewsets

from tracking.models import Transaction, Rate
from tracking.serializers import TransactionSerializer, RateSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self, *args, **kwargs):
        date = self.request.query_params.get('date', None)
        if date:
            return self.queryset.date(date)
        return super(TransactionViewSet, self).get_queryset(*args, **kwargs)
