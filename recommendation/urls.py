from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wine_recommend/', views.wine_recommend, name='wine_recommend'),
    path('wine_all', views.wine_all, name='wine_all'),
    path('wine_detail/<int:id>', views.wine_detail, name='wine_detail'),
    path('my_pic', views.my_pic, name='my_pic'),
]
