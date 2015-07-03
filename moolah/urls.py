from django.conf.urls import include, url
from django.contrib import admin
from allowance.views import (
    this_month,
    transactions,
    transactions_add,
    periods,
    periods_detail
)
from core.views import (
    profile,
    profile_success
)

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', this_month),
    url(r'^transactions/$', transactions),
    url(r'^transactions/add/$', transactions_add),
    url(r'^periods/$', periods),
    url(r'^periods/(?P<id>\d+)/$', periods_detail),
    url(r'^profile/$', profile),
    url(r'^profile/success/$', profile_success)
]
