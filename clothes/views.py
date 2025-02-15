from django.shortcuts import render
from . import models

def all_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.all().order_by('-id')
        context = {
            'all_clothes': query
        }
        return render(request, 'clothes/all_clothes.html', context)


def kid_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(tags__name='детская').order_by('-id')
        context = {
            'kid_clothes': query
        }
        return render(request, 'clothes/kid_clothes.html', context)


def teenage_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(tags__name='подростковая').order_by('-id')
        context = {
            'teenage_clothes': query
        }
        return render(request, 'clothes/teenage_clothes.html', context)

def adult_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(tags__name='взрослая').order_by('-id')
        context = {
            'adult_clothes': query
        }
        return render(request, 'clothes/adult_clothes.html', context)
