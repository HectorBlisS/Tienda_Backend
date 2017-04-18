from django.shortcuts import render
from rest_framework import viewsets
from listas.models import Mensaje
from .serializers import ListaSerializer
from rest_framework.permissions import IsAuthenticated


class ListasViewset(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = ListaSerializer
    permission_classes = [IsAuthenticated]