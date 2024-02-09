from ..models import UserGroup
from rest_framework import serializers

class WriteUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('guest_id', 'group_id')
        
class ReadUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = '__all__'