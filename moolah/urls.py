from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from api import ROUTER

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(ROUTER.urls)),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    url(r'^$', login_required(TemplateView.as_view(template_name='index.html')), name='home')
]
