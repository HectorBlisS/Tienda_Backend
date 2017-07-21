from rest_framework import serializers
from .models import Product, Category, MainProduct, PhysicalProducts


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    #category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

class MainProductSerializer(serializers.ModelSerializer):
	product = ProductSerializer(read_only=True)
	class Meta:
		model = MainProduct
		fields = '__all__'

class PhysicalProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalProducts
        fields = '__all__'