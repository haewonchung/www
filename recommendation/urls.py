from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    # path('wine/<int:id>',views.wineinfo,name="wineinfo"),

]
