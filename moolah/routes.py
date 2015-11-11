from rest_framework.routers import DefaultRouter

from tracking.views import TransactionViewSet, RateViewSet
from enjoying.views import PurchaseViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'rates', RateViewSet)
router.register(r'purchases', PurchaseViewSet)

urlpatterns = router.urls
