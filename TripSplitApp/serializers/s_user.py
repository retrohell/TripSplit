from django.contrib.auth.models import User
from rest_framework import serializers

class WriteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'id')
        
        # fields = '__all__'
    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data) # Traer el objeto que se esta creando
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('username', 'email')
        # fields = '__all__'
        exclude = ('password',)