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
