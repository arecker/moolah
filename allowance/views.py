from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Transaction, Period
from .forms import TransactionForm


@login_required
def this_month(request):
    sets = []
    for user in User.objects.all():
        sets.append({
            'user': user.__unicode__,
            'balance': Transaction.objects.balance(user=user),
            'transactions': Transaction.objects.latest_set_for_user(user)
        })
    return render_to_response('allowance/this_month.html', RequestContext(request, { 'sets': sets, 'period': Period.objects.latest() }))


@login_required
def transactions(request):
    if request.method == 'POST':
        f = TransactionForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/')
        return render_to_response('allowance/transaction_add.html', RequestContext(request, { 'form': f }))


@login_required
def transactions_add(request):
    return render_to_response('allowance/transaction_add.html', RequestContext(request, { 'form': TransactionForm() }))
