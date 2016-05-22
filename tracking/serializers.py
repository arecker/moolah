from rest_framework import serializers

from models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        exclude = ('allowance', )


class AllowanceTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        exclude = ()
