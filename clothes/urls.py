from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.AllClothesView.as_view(), name='all_clothes'),
    path('kid_clothes/', views.KidClothesView.as_view(), name='kid_clothes'),
    path('teenage_clothes/', views.TeenageClothesView.as_view(), name='teenage_clothes'),
    path('adult_clothes/', views.AdultClothesView.as_view(), name='adult_clothes')
]