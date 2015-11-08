from rest_framework import viewsets, views, response

from models import Transaction, Rate
from serializers import TransactionSerializer, RateSerializer


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


class SummaryView(views.APIView):
    def get(self, request):
        t = Transaction.objects
        data = {'rate': Rate.objects.total(),
                'day': t.today().total(),
                'week': t.last_week().total(),
                'month': t.last_month().total(),
                'year': t.last_year().total()}
        return response.Response(data)
