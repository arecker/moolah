from rest_framework.routers import DefaultRouter
from django.conf.urls import url

import views


router = DefaultRouter()
router.register(r'transactions', views.TransactionViewSet)
router.register(r'rates', views.RateViewSet)

urlpatterns = router.urls + [
    url(r'^summary/$', views.SummaryView.as_view()),
]
