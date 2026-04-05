from rest_framework import serializers
from .models import FinancialRecord

class FinancialRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialRecord
        fields = ['id', 'amount', 'record_type', 'category', 'date', 'notes', 'is_deleted', 'created_by']
        read_only_fields = ['created_by', 'is_deleted']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value