from datetime import timedelta

from rest_framework import views, response

from tracking.models import Rate, Transaction
from moolah.utils import get_timestamp


class SummaryView(views.APIView):
    def get(self, request):
        t = Transaction.objects

        data = {'rate': Rate.objects.total(),
                'day': t.today().total(),
                'week': t.last_week().total(),
                'month': t.last_month().total(),
                'year': t.last_year().total()}

        return response.Response(data)


class DailyTransactionReportView(views.APIView):
    def _days_before_today(self, n):
        return get_timestamp() - timedelta(n)

    def get(self, request):
        t = Transaction.objects
        today = get_timestamp()
        labels = ['Monday',
                  'Tuesday',
                  'Wednesday',
                  'Thursday',
                  'Friday',
                  'Saturday',
                  'Sunday']
        this_week = []
        last_week = []

        return response.Response({'labels': labels,
                                  'data': [this_week,
                                           last_week],
                                  'series': ['This Week', 'Last Week']})
