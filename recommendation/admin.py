from django.contrib import admin
from .models import wine, recommendation, wineTaste, food

# Register your models here.
admin.site.register(wine)
admin.site.register(recommendation)
admin.site.register(wineTaste)
admin.site.register(food)
