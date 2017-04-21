from rest_framework import viewsets
from rest_framework import views
from .models import Product
from .serializers import ProductSerializer
from .models import Document



class ProductsViewsets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


