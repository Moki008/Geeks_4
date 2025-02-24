from audioop import reverse
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from . import models, forms
from django.views import generic

from .models import Review


class CreateReviewView(generic.CreateView):
    template_name = 'create_review.html'
    form_class = forms.ReviewForm

    def form_valid(self, form):
        review = form.save(commit=False)
        review.save()
        book_id = review.book_id
        return redirect('books-detail', id=book_id)


class BookListView(generic.ListView):
    template_name = 'book.html'
    model = models.BookModel

    def get_queryset(self):
        return models.BookModel.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs['id']
        return models.BookModel.objects.get(id=book_id)


class AboutView(generic.View):
    def get(self, request):
        return HttpResponse('Я учусь на бэкенде')


class TextPhotoView(generic.View):
    def get(self, request):
        return HttpResponse('<h1>Cat</h1> '
                            '<img src="https://www.ferra.ru/imgs/2024/05/08/05/6460496/c2150453d059e8999c5f0b211ce334f7c869147c.jpg">')


class SystemTimeView(generic.View):
    def get(self, request):
        current_time = datetime.now()
        return HttpResponse(current_time)


class SearchView(generic.ListView):
    template_name = 'book.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return models.BookModel.objects.filter(title__icontains=query)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


