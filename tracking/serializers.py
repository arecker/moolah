from rest_framework import serializers

from models import Transaction, Rate

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        exclude = ()


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        exclude = ('amount_per_day', )
