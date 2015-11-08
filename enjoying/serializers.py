from rest_framework import serializers

from models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    def create(self, valid_data):  # attach current user
        valid_data['user'] = self.context.get('request').user
        return super(TransactionSerializer, self).create(valid_data)

    class Meta:
        model = Transaction
        exclude = ('user', )
