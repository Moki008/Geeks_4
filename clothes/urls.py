from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.all_clothes, name='all_clothes'),
    path('kid_clothes/', views.kid_clothes, name='kid_clothes'),
    path('teenage_clothes/', views.teenage_clothes, name='teenage_clothes'),
    path('adult_clothes/', views.adult_clothes, name='adult_clothes')
]