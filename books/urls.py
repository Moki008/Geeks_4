from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='books-detail'),
    path('search/', views.SearchView.as_view(), name='search'),

    path('about_me/', views.AboutView.as_view(), name='about_me'),
    path('text_and_photo/', views.TextPhotoView.as_view(), name='text_and_photo'),
    path('system_time/', views.SystemTimeView.as_view(), name='system_time'),
    path('create_review/', views.CreateReviewView.as_view(), name='create_review'),
]