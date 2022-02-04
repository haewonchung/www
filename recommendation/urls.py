from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('wine_detail/<int:id>', views.wine_detail, name='wine_detail'),
]
