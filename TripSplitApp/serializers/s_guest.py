from ..models import Guest
from rest_framework import serializers

class WriteGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('username', 'email', 'password', 'user')
        # fields = '__all__'

class ReadGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        # fields = ('username', 'email')
        # fields = '__all__'
        exclude = ('password',)