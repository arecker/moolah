from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from .models import MonthlyBudget, MonthlyTransaction
from decimal import Decimal


class BudgetResponse(object):
    def __init__(self, pk, request):
        try:
            budget = MonthlyBudget.objects.get(pk=pk)
            trans_class = MonthlyTransaction
        except MonthlyBudget.DoesNotExist:
            pass
        if budget.shared:
            return self._build_shared_budget_response(
                budget,
                trans_class,
                request
            )
        return self._build_individual_budget_response(
            budget,
            trans_class,
            request
        )

    def _format_balance(self, dec):
        if dec < Decimal(0):
            return '- ${0}'.format(-1 * dec)
        return '${0}'.format(dec)

    def _build_individual_budget_response(self, budget, trans_class, request):
        sets = []
        for u in User.objects.all():
            transactions = trans_class.objects.latest_period(
                budget=budget
            ).filter(user=u)
            sets.append({
                'user': u,
                'transactions': transactions,
                'balance': self._format_balance(transactions.balance())
            })

        return render_to_response(
            'spending/individual_budget_detail.html',
            RequestContext(request, {
                'budget': budget,
                'sets': sets
            })
        )

    def _build_shared_budget_response(self, budget, trans_class, request):
        transactions = trans_class.objects.latest_period(budget=budget)
        return render_to_response(
            'spending/shared_budget_detail.html',
            RequestContext(request, {
                'budget': budget,
                'transactions': transactions,
                'balance': self._format_balance(transactions.balance())
            })
        )
