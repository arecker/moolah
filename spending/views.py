from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from .models import MonthlyBudget, MonthlyTransaction


@login_required
def budget_detail(request, pk=None):
    try:
        budget = MonthlyBudget.objects.get(pk=pk)
        if budget.shared:
            return _return_shared_budget_detail(request, budget)
        else:
            return _return_individual_budget_detail(request, budget)
    except (MonthlyBudget.DoesNotExist):
        # todo: log it
        raise Http404


def _return_individual_budget_detail(request, budget):
    users = User.objects.all()
    sets = []
    for u in users:
        transactions = MonthlyTransaction.objects.latest_period(
            budget=budget
        ).filter(user=u)
        sets.append({
            'user': u,
            'transactions': transactions,
            'balance': transactions.balance()
        })

    return render_to_response(
        'spending/individual_budget_detail.html',
        RequestContext(request, {
            'budget': budget,
            'sets': sets
        })
    )


def _return_shared_budget_detail(request, budget):
    transactions = MonthlyTransaction.objects.latest_period(budget=budget)
    return render_to_response(
        'spending/shared_budget_detail.html',
        RequestContext(request, {
            'budget': budget,
            'transactions': transactions,
            'balance': transactions.balance()
        })
    )
