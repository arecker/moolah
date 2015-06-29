from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required
def test_response(request):
    return HttpResponse('working, mate')


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', test_response)
]
