from django.contrib import admin
from .models import Product, Category, Document


class ProductAdmin(admin.ModelAdmin):
	list_display = ['id','name']

admin.site.register(Product, ProductAdmin)

class DocumentAdmin(admin.ModelAdmin):
	list_display = ['id','title']

admin.site.register(Document, DocumentAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id','name']
	prepopulated_fields={'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
