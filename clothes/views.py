from django.shortcuts import render
from . import models
from django.views import generic


class AllClothesView(generic.ListView):
    template_name = 'clothes/all_clothes.html'
    context_object_name = 'all_clothes'

    def get_queryset(self):
        return models.Clothes.objects.all().order_by('-id')


class KidClothesView(generic.ListView):
    template_name = 'clothes/kid_clothes.html'
    context_object_name = 'kid_clothes'

    def get_queryset(self):
        return models.Clothes.objects.filter(tags__name='детская').order_by('-id')


class TeenageClothesView(generic.ListView):
    template_name = 'clothes/teenage_clothes.html'
    context_object_name = 'teenage_clothes'

    def get_queryset(self):
        return models.Clothes.objects.filter(tags__name='подростковая').order_by('-id')


class AdultClothesView(generic.ListView):
    template_name = 'clothes/adult_clothes.html'
    context_object_name = 'adult_clothes'

    def get_queryset(self):
        return models.Clothes.objects.filter(tags__name='взрослая').order_by('-id')
