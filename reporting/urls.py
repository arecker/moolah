from django.conf.urls import url

import views


urlpatterns = [
    url(r'^summary/$', views.SummaryView.as_view(), name='summary')
]
