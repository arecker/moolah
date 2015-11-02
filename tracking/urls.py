from django.conf.urls import url

import views


urlpatterns = [url(r'^$',
                   views.Summary.as_view(),
                   name='summary'),
               url(r'^today/$',
                   views.Today.as_view(),
                   name='today')]
