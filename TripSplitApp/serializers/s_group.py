from ..models import Group
from rest_framework import serializers

class WriteGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)
        
class ReadGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'