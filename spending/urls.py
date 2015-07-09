from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^$', views.index, name='spending_index'),
    url(r'^(?P<pk>[^/]+)/$', views.budget_detail, name='budget_detail')
]
