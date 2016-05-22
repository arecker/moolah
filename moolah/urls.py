from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from api import ROUTER

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(ROUTER.urls)),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home')
]
