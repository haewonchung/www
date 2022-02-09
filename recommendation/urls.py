from django.urls import path
from . import views

app_name = 'recommendation'

urlpatterns = [
    path('', views.home, name='home'),
    path('wine-recommend/', views.wine_recommend, name='wine-recommend'),
    path('wine-all/', views.wine_all, name='wine-all'),
    path('wine-detail/<int:id>/', views.wine_detail, name='wine-detail'),
    path('my-pick/', views.my_pick, name='my-pick'),
    path('wine-save-toggle/<int:wine_id>/<str:check_page>/', views.wine_save_toggle, name="wine-save-toggle"),
    path('search/', views.search, name="search"),
]
