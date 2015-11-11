from django.conf.urls import url

import views


urlpatterns = [
    url(r'^summary/$', views.SummaryView.as_view(), name='summary'),
    url(r'^daily_transaction/$', views.DailyTransactionReportView.as_view(), name='daily_transaction')
]
