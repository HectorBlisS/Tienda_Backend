from rest_framework import serializers
from listas.models import Mensaje


class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ['id', 'message', 'perro']