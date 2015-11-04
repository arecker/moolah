from dateutil import parser

from rest_framework import viewsets

from models import Transaction, Rate
from serializers import TransactionSerializer, RateSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self, *args, **kwargs):
        date = (self
                .request
                .query_params
                .get('date', None))

        if date:
            parsed = parser.parse(date.replace('"', ''))
            return self.queryset.date(parsed)

        return super(TransactionViewSet, self).get_queryset(*args, **kwargs)
