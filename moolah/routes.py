from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from tracking.views import TransactionViewSet, RateViewSet, SummaryView
from enjoying.views import PurchaseViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'rates', RateViewSet)
router.register(r'purchases', PurchaseViewSet)


urlpatterns = router.urls + [
    url(r'^summary/$', SummaryView.as_view()),
]
