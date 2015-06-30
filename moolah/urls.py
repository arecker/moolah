from django.conf.urls import include, url
from django.contrib import admin
from allowance import views


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.this_month),
    url(r'^transactions/$', views.transactions)
]
