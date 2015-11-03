from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('tracking.urls')),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', login_required(TemplateView.as_view(template_name='index.html')))
]
