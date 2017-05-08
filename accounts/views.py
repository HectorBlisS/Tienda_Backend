from django.shortcuts import render
from rest_framework import viewsets
from listas.models import Mensaje
from .serializers import ListaSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User

class ListasViewset(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = ListaSerializer
    permission_classes = [IsAuthenticated]

class UserCreateView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
