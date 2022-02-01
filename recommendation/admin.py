from django.contrib import admin
from .models import Wine, WineProfile, Food


# Register your models here.
admin.site.register(Wine)
admin.site.register(WineProfile)
admin.site.register(Food)

