from django.urls import path
from . import views

urlpatterns = [
    path('litrez_list/', views.LitrezListView.as_view(), name="litrez_list"),
    path('litrez_parsing/', views.ParserFormView.as_view(), name="parser"),
    path('rezka_list/', views.RezkaListView.as_view(), name="rezka_list"),
]