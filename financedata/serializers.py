# serializers.py

from rest_framework import serializers
from .models import Financedata


class FinanceDataSerializer(serializers.ModelSerializer):

    uploaded_by = serializers.ReadOnlyField(source='uploaded_by.username')

    class Meta:
        model = Financedata
        fields = [
            'id',
            'title',
            'description',
            'amount',
            'category',
            'uploaded_by',
            'uploaded_at'
        ]