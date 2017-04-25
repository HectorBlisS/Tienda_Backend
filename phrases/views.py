from django.shortcuts import render, get_object_or_404, HttpResponse
from rest_framework.views import APIView
from .models import Today, Frase
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import TodaySerializer, FraseSerializer

#tarea
from .tasks import change_frase

class FraseView(APIView):
    #permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        today = Today.objects.get(id=1)
        frase = today.frase
        serializer = FraseSerializer(frase)
        frase = serializer.data
        #change_frase.delay()
        return Response(frase)

