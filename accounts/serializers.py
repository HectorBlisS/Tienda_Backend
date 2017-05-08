from rest_framework import serializers
from listas.models import Mensaje
from django.contrib.auth.models import User


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ['id', 'message', 'perro']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        write_only_fields = ('password',)
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
