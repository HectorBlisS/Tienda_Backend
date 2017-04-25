from django.contrib import admin
from .models import Today, Frase

class TodayAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'id']

admin.site.register(Today, TodayAdmin)
admin.site.register(Frase)