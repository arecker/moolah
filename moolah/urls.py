from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views import i18n
from django.shortcuts import redirect
from rest_framework_jwt.views import obtain_jwt_token

from api import ROUTER


def logout(*args, **kwargs):
    auth_views.logout(*args, **kwargs)
    return redirect('login')


js_info_dict = {
    'packages': ('recurrence', ),
}


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(ROUTER.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^jsi18n/$', i18n.javascript_catalog, js_info_dict),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^$', login_required(TemplateView.as_view(template_name='index.html')), name='home')
]
