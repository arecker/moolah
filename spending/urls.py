from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='spending_index'),
    url(
        r'^budget/(?P<pk>[^/]+)/$',
        views.budget_detail,
        name='budget_detail'
    ),
    url(
        r'^transaction/add/(?P<pk>[^/]+)/$',
        views.transaction_add,
        name='add_transaction'
    )
]
