from django.urls import path
from . import views, models

urlpatterns = [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/',views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('add_recipe/', views.RecipeCreateView.as_view(), name='add_recipe'),
    path('recipe/<int:pk>/add_ingredient/', views.IngredientCreateView.as_view(), name='add_ingredient'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='delete_recipe'),
]