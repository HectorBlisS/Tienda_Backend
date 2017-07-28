#from django.shortcuts import render, HttpResponse
from social_api.settings import BASE_DIR 
from django.views.generic import View
from rest_framework import permissions
from rest_framework.views import APIView
from products.models import Product
from django.http import HttpResponse

""" Usando gsutil """

import subprocess

class OwnerMixin(object):
    def get_queryset(self):
        qs = super(OwnerMixin, self).get_queryset()
        return qs.filter(user=self.request.user)


class GetSignedUrl(APIView):
	#permission_classes = (permissions.IsAuthenticated,)

	def get(self, request, doc_id):
		product = Product.objects.get(id=doc_id)
		if product.users.filter(id=request.user.id).exists():
			result = subprocess.run(["gsutil", "signurl", "-d", "10m", BASE_DIR+"/tienda-eric-e3120f4dca2e.json", "gs://tienda-eric/"+product.fileName], stdout=subprocess.PIPE)
			result = result.stdout.decode("utf-8").split(" ")
			print("final", result)
			return HttpResponse(result[14][9:])
			

		return HttpResponse("No haz comprado este articulo")

