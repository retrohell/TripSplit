from ..models import ExpenseParticipant
from rest_framework import serializers

class WriteExpenseParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseParticipant
        fields = ('expense_id', 'participant_id')
        
class ReadExpenseParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseParticipant
        fields = '__all__'
