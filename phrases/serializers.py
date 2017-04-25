from rest_framework import serializers
from .models import Today, Frase


class FraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frase
        fields = ['id', 'titulo', 'body', 'ref']


class TodaySerializer(serializers.ModelSerializer):
    frase = FraseSerializer(read_only=True)

    class Meta:
        model = Today
        fields = '__all__'


