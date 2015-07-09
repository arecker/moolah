from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.template import RequestContext
from .models import MonthlyBudget, MonthlyTransaction


@login_required
def budget_detail(request, pk=None):
    try:
        budget = MonthlyBudget.objects.get(pk=pk)
        transactions = MonthlyTransaction.objects.latest_period(budget=budget)
    except (MonthlyBudget.DoesNotExist):
        # todo: log it
        raise Http404
    return render_to_response(
        'spending/budget_detail.html',
        RequestContext(request, {
            'budget': budget,
            'transactions': transactions
        })
    )
