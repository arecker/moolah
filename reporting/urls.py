from django.conf.urls import url

from reporting import views


urlpatterns = [
    url(r'^summary/$', views.SummaryView.as_view(), name='summary'),
    url(r'^daily_transaction/$', views.DailyTransactionReportView.as_view(), name='daily_transaction'),
    url(r'^yearly_savings_daily/$', views.YearlySavingReflectionReportView.as_view(), name='yearly_savings_daily'),
    url(r'^rate_breakdown/$', views.RateBreakdownReportView.as_view(), name='rate_breakdown')
]
