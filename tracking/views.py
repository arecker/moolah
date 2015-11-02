from django.views.generic import TemplateView

from models import Transaction, Rate


class Summary(TemplateView):
    template_name = 'tracking/summary.html'

    def get_context_data(self, *args, **kwargs):
        transactions = Transaction.objects
        context = super(Summary, self).get_context_data(*args, **kwargs)
        context['rate'] = Rate.objets.total()
        context['today'] = transactions.today().total()
        context['week'] = transactions.last_week().total()
        context['month'] = transactions.last_month().total()
        context['year'] = transactions.last_year().total()
        return context
