from django.shortcuts import (
    render_to_response,
    RequestContext,
    HttpResponseRedirect
)
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Account


@login_required
def profile(request):
    if request.method == 'POST':
        form = forms.AccountForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect('/')
    else:
        form = forms.AccountForm(
            instance=Account.objects.get(user=request.user)
        )
    return render_to_response(
        'registration/profile.html',
        RequestContext(request, {
            'form': form
        })
    )
