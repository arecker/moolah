from rest_framework import views, response

from tracking.models import Rate, Transaction


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
    def get(self, request):
        t = Transaction.objects
        labels = []
        data = []
        number_format_dict = {'0': 'Today',
                              '1': 'Yesterday',
                              '2': '2 days ago',
                              '3': '3 days ago',
                              '4': '4 days ago',
                              '5': '5 days ago',
                              '6': '6 days ago',
                              '7': '7 days ago'}
        for n in range(7):
            labels.append(number_format_dict.get(str(n)))
            data.append(t.days_ago(n).total())

        return response.Response({'labels': labels,
                                  'data': [data],
                                  'series': ['This Week']})
