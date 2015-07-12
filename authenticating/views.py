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
    instance = Account.objects.get(user=request.user)
    if request.method == 'POST':
        form = forms.AccountForm(
            request.POST,
            request.FILES,
            instance=instance
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.AccountForm(
            instance=instance
        )
    return render_to_response(
        'registration/profile.html',
        RequestContext(request, {
            'form': form
        })
    )
