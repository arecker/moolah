from rest_framework import serializers

from models import Transaction, Rate

class TransactionSerializer(serializers.ModelSerializer):

    def create(self, valid_data):
        valid_data['amount'] = valid_data['amount'] * -1
        return super(TransactionSerializer, self).create(valid_data)

    class Meta:
        model = Transaction
        exclude = ()


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        exclude = ('amount_per_day', )
