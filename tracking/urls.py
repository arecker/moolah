from django.conf.urls import url

import views


urlpatterns = [url(r'^$',
                   views.Summary.as_view(),
                   name='summary')]
