from django.shortcuts import render, HttpResponse
from social_api.settings import BASE_DIR 
from django.views.generic import View
from rest_framework import permissions
from rest_framework.views import APIView

""" Usando gsutil """

import subprocess
class GetSignedUrl(APIView):
	permission_classes = (permissions.IsAuthenticated,)

	def get(self, request):

		result = subprocess.run(["gsutil", "signurl", "-d", "10m", BASE_DIR+"/tienda-eric-e3120f4dca2e.json", "gs://tienda-eric/BRIEF.pdf"], stdout=subprocess.PIPE)
		result = result.stdout.decode("utf-8").split(" ")
		# print(request.authenticators[1].__dict__)
		return HttpResponse(result[3][9:])

