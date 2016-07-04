from rest_framework import serializers

from models import Transaction, Allowance


class TransactionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['amount'] = validated_data['amount'] * -1
        return super(TransactionSerializer, self).create(validated_data)

    class Meta:
        model = Transaction
        exclude = ('allowance', 'timestamp')


class AllowanceTransactionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['amount'] = validated_data['amount'] * -1
        user = self.context['request'].user
        validated_data['allowance'] = Allowance.objects.get(user=user)
        return super(AllowanceTransactionSerializer, self).create(validated_data)

    class Meta:
        model = Transaction
        exclude = ('timestamp', 'allowance')
