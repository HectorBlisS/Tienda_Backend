from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from .models import Document

#permisos
from rest_framework import permissions


class ProductsViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DocumentView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    """
    Redirect to a protected file
    """
    def get(self, request, doc_id):
        document = Document.objects.get(id=doc_id)
        response = HttpResponse()
        response.content = document.file.read()
        response["Content-Disposition"] = "attachment; filename={0}".format(
            document.pretty_name)
        return response
