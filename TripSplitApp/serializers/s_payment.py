from ..models import Payment
from rest_framework import serializers

class WritePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('payer_id', 'receiver_id', 'amount')
        
class ReadPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'