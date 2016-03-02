from datetime import timedelta

from rest_framework import views, response
from dateutil.relativedelta import relativedelta, MO

from tracking.models import Rate, Transaction
from enjoying.models import Purchase
from moolah.utils import get_timestamp


class SummaryView(views.APIView):
    def get(self, request):
        t = Transaction.objects

        balance = Purchase.objects.current_user(request)

        data = {'rate': Rate.objects.total(),
                'day': t.today().total(),
                'week': t.last_week().total(),
                'month': t.last_month().total(),
                'year': t.last_year().total(),
                'balance': balance.total()}

        return response.Response(data)


class DailyTransactionReportView(views.APIView):
    def _get_week_dates(self, weeks=-1):
        today = get_timestamp()
        monday = today + relativedelta(weekday=MO(weeks))
        return [monday + timedelta(days=n)
                for n in range(7)]

    def get(self, request):
        t = Transaction.objects
        labels = ['Monday',
                  'Tuesday',
                  'Wednesday',
                  'Thursday',
                  'Friday',
                  'Saturday',
                  'Sunday']

        this_week = [t.date(d).total()
                     for d in self._get_week_dates()]

        last_week = [t.date(d).total()
                     for d in self._get_week_dates(-2)]

        return response.Response({'labels': labels,
                                  'data': [this_week,
                                           last_week],
                                  'series': ['This Week', 'Last Week']})


class YearlySavingReflectionReportView(views.APIView):
    def get(self, request):
        t = Transaction.objects
        today = get_timestamp()
        labels = range(100, -1, -1)
        year_before_then = timedelta(days=-365)
        dates = [today + timedelta(days=-n) for n in labels]
        data = [t.date_range((d + year_before_then), d).total()
                for d in dates]
        return response.Response({'labels': labels,
                                  'data': [data],
                                  'series': []})


class RateBreakdownReportView(views.APIView):
    def get(self, request):
        data = []
        labels = []
        for rate in Rate.objects.all():
            data.append(rate.amount_per_day)
            labels.append(rate.description)
        return response.Response({'labels': labels,
                                  'data': data})
