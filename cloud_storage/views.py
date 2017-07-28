from django.shortcuts import render, HttpResponse
from django.conf import settings 
from django.views.generic import View
from rest_framework import permissions
from rest_framework.views import APIView
from products.models import Product

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
		print("nombre del producto", product.fileName)
		if product.users.filter(id=request.user.id).exists():
			try:
				result = subprocess.call(["gsutil", "signurl", "-d", "10m", settings.BASE_DIR+"/tienda-eric-e3120f4dca2e.json", "gs://tienda-eric/"+product.fileName], stdout=subprocess.PIPE)
				result = result.stdout.decode("utf-8").split(" ")
				return HttpResponse(result[3][9:])
			except Exception as e:
				print (e)
			

		return HttpResponse("No haz comprado este articulo")

