from rest_framework import viewsets

from enjoying.models import Purchase
from enjoying.serializers import PurchaseSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def get_queryset(self, *args, **kwargs):
        return self.queryset.current_user(self.request).this_month()
