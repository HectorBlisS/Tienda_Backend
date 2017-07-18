from django.contrib import admin
from .models import Product, Category, Document, MainProduct


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


class MainProductAdmin(admin.ModelAdmin):
	def has_add_permission(self, request):
		count = MainProduct.objects.all().count()
		if count == 0:
			return True
		return False

admin.site.register(MainProduct, MainProductAdmin)
