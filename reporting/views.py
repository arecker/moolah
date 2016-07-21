import collections

from dateutil.relativedelta import MO, relativedelta
from django.utils import timezone
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.viewsets import ViewSet

from tracking.models import Allowance, Rate, Transaction


class ReportViewSet(ViewSet):
    def list(self, *args, **kwargs):
        return Response({
            'summary': reverse_lazy('reports-summary', request=self.request),
            'savings': reverse_lazy('reports-savings', request=self.request),
            'rates': reverse_lazy('reports-rates', request=self.request),
            'week': reverse_lazy('reports-week', request=self.request),
            'allowance': reverse_lazy('reports-allowance', request=self.request),
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

    @list_route(methods=['get'], url_path='savings')
    def savings(self, *args, **kwargs):
        transactions = Transaction.objects.without_allowance()
        today = timezone.now()
        labels = range(100, -1, -1)
        year_before_then = timezone.timedelta(days=-365)
        dates = [today + timezone.timedelta(days=-n) for n in labels]
        data = [transactions.date_range((d + year_before_then), d).total() for d in dates]
        return Response({
            'labels': labels,
            'data': [data],
            'series': []
        })

    @list_route(methods=['get'], url_path='week')
    def week_breakdown(self, *args, **kwargs):
        today = timezone.now()

        def get_week_dates(weeks=-1):
            monday = today + relativedelta(weekday=MO(weeks))
            return [
                monday + timezone.timedelta(days=n)
                for n in range(7)
            ]

        t = Transaction.objects.without_allowance()

        labels = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]

        this_week = [
            t.date(d).total()
            for d in get_week_dates()
        ]

        last_week = [
            t.date(d).total()
            for d in get_week_dates(-2)
        ]

        return Response({
            'labels': labels,
            'data': [this_week, last_week],
            'series': ['This Week', 'Last Week']
        })

    @list_route(methods=['get'], url_path='rates')
    def rates_breakdown(self, *args, **kwargs):
        rates = Rate.objects.all()

        income = rates.filter(amount_per_day__gt=0)
        expense = rates.exclude(pk__in=income)

        return Response({
            'income': {
                'labels': income.values_list('description', flat=True),
                'data': income.values_list('amount_per_day', flat=True)
            },
            'expense': {
                'labels': expense.values_list('description', flat=True),
                'data': expense.values_list('amount_per_day', flat=True)
            },
            'total': {
                'labels': ['Income', 'Expenses'],
                'data': [
                    income.total() or 0,
                    abs(expense.total() or 0)
                ]
            }
        })

    @list_route(methods=['get'], url_path='allowance')
    def allowance_balances(self, request, *args, **kwargs):
        allowance = Allowance.objects.get(user=request.user)
        transactions = Transaction.objects.filter(allowance=allowance)

        this_month = timezone.now().replace(day=1) + relativedelta(months=1) - relativedelta(days=1)
        last_month = this_month - relativedelta(months=1)
        month_before = this_month - relativedelta(months=2)
        month_before_before = this_month - relativedelta(months=3)

        response = []

        for period in [this_month, last_month, month_before, month_before_before]:
            response.append((
                period.strftime('%B'),
                transactions.date_range(
                    start_of_day=None,
                    end_of_day=period
                ).total()
            ))

        return Response(collections.OrderedDict(response))
