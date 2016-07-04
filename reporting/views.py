from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.decorators import list_route

from tracking.models import Transaction, Rate


class ReportViewSet(ViewSet):
    def list(self, *args, **kwargs):
        return Response({
            'summary': reverse_lazy('reports-summary', request=self.request)
        })

    @list_route(methods=['get'], url_path='summary')
    def summary(self, *args, **kwargs):
        transactions = Transaction.objects.without_allowance()
        return Response({
            'today': transactions.today().total(),
            'week': transactions.last_week().total(),
            'month': transactions.last_month().total(),
            'year': transactions.last_year().total(),
            'daily': Rate.objects.total()
        })
