from rest_framework.routers import DefaultRouter

from tracking.views import TransactionViewSet, AllowanceTransactionViewSet


ROUTER = DefaultRouter()
ROUTER.register('transactions', TransactionViewSet)
ROUTER.register('purchases', AllowanceTransactionViewSet, 'purchase')
