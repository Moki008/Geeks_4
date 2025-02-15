from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models, forms


def book_list_view(request):
    if request.method == 'GET':
        form = forms.ReviewForm()
        query = models.BookModel.objects.all()
        context_object = {
            'book': query,
            'form': form

        }
        return render(request, template_name='book.html', context=context_object)
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Review added')
        return HttpResponse('Error')



def book_detail_view(request, id):
    if request.method == 'GET':
        query = get_object_or_404(models.BookModel, id=id)
        context_object = {
            'book_id': query
        }
        return render(request, template_name='book_detail.html', context=context_object)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Я учусь на бэкенде')


def text_and_photo(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Cat</h1> '
                            '<img src="https://www.ferra.ru/imgs/2024/05/08/05/6460496/c2150453d059e8999c5f0b211ce334f7c869147c.jpg">')


def system_time(request):
    if request.method == 'GET':
        current_time = datetime.now()
        return HttpResponse(current_time)
