from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wine-recommend/', views.wine_recommend, name='wine-recommend'),
    path('wine-all/', views.wine_all, name='wine-all'),
    path('wine-detail/<int:id>/', views.wine_detail, name='wine-detail'),
    path('my-pic/<int:id>/', views.my_pic, name='my-pic'),
]
