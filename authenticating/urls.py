from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'login/$', auth_views.login),
    url(r'logout/$', auth_views.logout),
    url(r'profile/$', views.profile, name="profile")
]
