from rest_framework import serializers

from models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    def create(self, valid_data):  # attach current user
        valid_data['user'] = self.context.get('request').user
        return super(PurchaseSerializer, self).create(valid_data)

    class Meta:
        model = Purchase
        exclude = ('user', )
