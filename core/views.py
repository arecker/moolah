from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST,
            instance=UserProfile.objects.get(user=request.user)
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile/success')
    else:
        form = UserProfileForm(
            instance=UserProfile.objects.get(user=request.user)
        )
    return render_to_response(
        'registration/profile.html',
        RequestContext(request, {'form': form})
    )


@login_required
def profile_success(request):
    return HttpResponseRedirect('/profile/')
