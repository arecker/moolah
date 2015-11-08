from rest_framework.routers import DefaultRouter

import views


router = DefaultRouter()
router.register(r'purchases', views.TransactionViewSet, 'purchases')


urlpatterns = router.urls
