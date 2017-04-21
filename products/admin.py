from django.contrib import admin
from .models import Product, Category, Document

admin.site.register(Product)

admin.site.register(Document)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id','name']
	prepopulated_fields={'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
