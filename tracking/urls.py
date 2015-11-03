from rest_framework.routers import DefaultRouter

import views


router = DefaultRouter()
router.register(r'transactions', views.TransactionViewSet)
router.register(r'rates', views.RateViewSet)

urlpatterns = router.urls
