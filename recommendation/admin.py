from django.contrib import admin
from .models import Wine, WineProfile, Food, WineRecommend, WineFood

# Register your models here.
admin.site.register(Wine)
admin.site.register(WineProfile)
admin.site.register(WineRecommend)
admin.site.register(WineFood)
admin.site.register(Food)

