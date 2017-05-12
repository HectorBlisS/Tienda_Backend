from django.shortcuts import render
from rest_framework import viewsets
from listas.models import Mensaje
from .serializers import ListaSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView, ListAPIView
from django.contrib.auth.models import User
from rest_framework.views import APIView


class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(id=self.request.user.id)


class ListasViewset(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = ListaSerializer
    permission_classes = [IsAuthenticated]


class UserCreateView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserData(OwnerMixin, ListAPIView):
	serializer_class = UserSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return [self.request.user]


class UserEdit(OwnerMixin, RetrieveUpdateAPIView):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	permission_classes = [IsAuthenticated]
