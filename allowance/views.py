from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from decimal import Decimal
from .models import Transaction
from .forms import TransactionForm


def calculate_balance(ts):
    try:
        pos = Decimal(ts.filter(negative=False).aggregate(Sum('amount'))['amount__sum'])
    except:
        pos = Decimal(0)
    try:
        neg = Decimal(ts.filter(negative=True).aggregate(Sum('amount'))['amount__sum'])
    except:
        neg = Decimal(0)
    return pos - neg


@login_required
def this_month(request):
    sets = []
    for user in User.objects.all():
        ts = Transaction.objects.latest_set_for_user(user)
        sets.append({
            'user': user.__unicode__,
            'balance': calculate_balance(ts),
            'transactions': ts
        })
    return render_to_response('allowance/this_month.html', RequestContext(request, {
        'sets': sets,
        'form': TransactionForm(),
    }))


@login_required
def transactions(request):
    if request.method == 'POST':
        f = TransactionForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/')
