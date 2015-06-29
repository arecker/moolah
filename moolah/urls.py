from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
