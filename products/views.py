from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Product, MainProduct, Document, Category
from .serializers import ProductSerializer, CategorySerializer, MainProductSerializer
from rest_framework import generics
from rest_framework.generics import ListAPIView

#permisos
from rest_framework import permissions


class ProductListOwner(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.products.all()
        

class ProductsViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all().filter(available=True)
    serializer_class = ProductSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DocumentView(APIView):
    #permission_classes = (permissions.IsAuthenticated,)
    """
    Redirect to a protected file
    """
    def get(self, request, doc_id):
        document = Document.objects.get(id=doc_id)
        product = Product.objects.get(id=doc_id)
        if product.users.filter(id=request.user.id).exists():
            response = HttpResponse()
            response.content = document.file.read()
            response["Content-Disposition"] = "attachment; filename={0}".format(
                document.pretty_name)
            return response
        return HttpResponse("No haz comprado este articulo")



class MainProductView(ListAPIView):
    queryset = MainProduct.objects.all()
    serializer_class = MainProductSerializer
