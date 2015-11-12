from django.conf.urls import url

import views


urlpatterns = [
    url(r'^summary/$', views.SummaryView.as_view(), name='summary'),
    url(r'^daily_transaction/$', views.DailyTransactionReportView.as_view(), name='daily_transaction'),
    url(r'^yearly_savings_daily/$', views.YearlySavingReflectionReportView.as_view(), name='yearly_savings_daily')
]
