from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Transaction, Period
from .forms import TransactionForm


def display_period(id=None):
    if not id:
        period = Period.objects.latest()
    else:
        period = Period.objects.get(pk=id)
    sets = []
    for user in User.objects.all():
        sets.append({
            'user': user,
            'balance': Transaction.objects.balance(user=user),
            'transactions': Transaction.objects.latest_set_for_user(user)
        })
    return sets, period


@login_required
def this_month(request):
    sets, period = display_period()
    return render_to_response(
        'allowance/this_month.html',
        RequestContext(request, {'sets': sets, 'period': period})
    )


@login_required
def transactions(request):
    if request.method == 'POST':
        f = TransactionForm(request.POST)
        if f.is_valid():
            f.cleaned_data['user'] = request.user
            f.instance.user = request.user
            f.save()
            return HttpResponseRedirect('/')
        return render_to_response(
            'allowance/transaction_add.html',
            RequestContext(request, {'form': f})
        )


@login_required
def transactions_add(request):
    return render_to_response(
        'allowance/transaction_add.html',
        RequestContext(request, {'form': TransactionForm()})
    )


@login_required
def periods(request):
    return render_to_response(
        'allowance/periods.html',
        RequestContext(request, {'periods': Period.objects.all()})
    )


@login_required
def periods_detail(request, id):
    sets, period = display_period(id=id)
    return render_to_response(
        'allowance/this_month.html',
        RequestContext(request, {'sets': sets, 'period': period})
    )
