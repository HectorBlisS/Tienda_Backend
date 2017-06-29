from social_api import settings
from django.views.generic import View
from django.shortcuts import render, HttpResponse
from rest_framework import permissions
from rest_framework.views import APIView


# Create your views here.

""" Usando gsutil """

import subprocess
class GetSignedUrl(APIView):
	permission_classes = (permissions.IsAuthenticated,)

	def get(self, request):

		if product.users.filter(id=request.user.id).exists():
			result = subprocess.run(["gsutil", "signurl", "-d", "10m", settings.BASE_DIR+"/tienda-eric-e3120f4dca2e.json", "gs://tienda-eric/BRIEF.pdf"], stdout=subprocess.PIPE)
			result = result.stdout.decode("utf-8").split(" ")
			return HttpResponse(result[3][9:])

		return HttpResponse("Producto no adquirido")

