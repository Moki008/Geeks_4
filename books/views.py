from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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

