from rest_framework import serializers

from models import Allowance, Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    def create(self, valid_data):
        request = self.context.get('request')
        valid_data['allowance'] = Allowance.objects.current_user(request)
        valid_data['amount'] = valid_data['amount'] * -1
        return super(PurchaseSerializer, self).create(valid_data)

    class Meta:
        model = Purchase
        exclude = ('allowance', )
