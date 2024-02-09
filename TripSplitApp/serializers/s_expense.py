from ..models import Expense
from rest_framework import serializers

class WriteExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('payer', 'amount', 'description', 'created_at')
        
class ReadExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        exclude = ('updated_at', 'created_at')