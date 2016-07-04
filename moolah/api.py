from rest_framework.routers import DefaultRouter

from tracking.views import TransactionViewSet, AllowanceTransactionViewSet
from reporting.views import ReportViewSet


ROUTER = DefaultRouter()
ROUTER.register('transactions', TransactionViewSet)
ROUTER.register('purchases', AllowanceTransactionViewSet, 'purchase')
ROUTER.register('reports', ReportViewSet, 'reports')
