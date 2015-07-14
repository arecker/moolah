from django.shortcuts import render_to_response, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from .models import Budget, Transaction
from .forms import MonthlyTransactionForm
from moolah.mixins import LoginRequiredMixin
from decimal import Decimal


@login_required
def index(request):
    return render_to_response(
        'spending/index.html',
        RequestContext(request, {})
    )


@login_required
def budget_detail(request, pk=None):
    try:
        budget = Budget.objects.get(pk=pk)
        if budget.shared:
            return _return_shared_budget_detail(request, budget)
        else:
            return _return_individual_budget_detail(request, budget)
    except (Budget.DoesNotExist):
        raise Http404


def _return_individual_budget_detail(request, budget):
    users = User.objects.all()
    sets = []
    for u in users:
        transactions = Transaction.objects.latest_period(
            budget=budget
        ).filter(user=u)
        sets.append({
            'user': u,
            'transactions': transactions,
            'balance': _format_balance(transactions.balance())
        })

    return render_to_response(
        'spending/individual_budget_detail.html',
        RequestContext(request, {
            'budget': budget,
            'sets': sets
        })
    )


def _return_shared_budget_detail(request, budget):
    transactions = Transaction.objects.latest_period(budget=budget)
    return render_to_response(
        'spending/shared_budget_detail.html',
        RequestContext(request, {
            'budget': budget,
            'transactions': transactions,
            'balance': _format_balance(transactions.balance())
        })
    )


def _format_balance(dec):
    if dec < Decimal(0):
        return '- ${0}'.format(-1 * dec)
    return '${0}'.format(dec)


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction


@login_required
def transaction_add(request, pk):
    if request.method == 'POST':
        form = MonthlyTransactionForm(
            request.POST,
        )
        if form.is_valid():
            form.save(
                request.user,
                pk
            )
            return HttpResponseRedirect(
                Budget.objects.get(
                    pk=pk).get_absolute_url()
            )
    else:
        form = MonthlyTransactionForm()
    return render_to_response(
        'spending/transaction_add.html',
        RequestContext(request, {
            'form': form,
            'budget': Budget.objects.get(pk=pk)
        })
    )
