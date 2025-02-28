from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy

from . import models, forms
from django.views import generic

class RecipeListView(generic.ListView):
    model = models.Recipe
    template_name = 'food/recipe_list.html'
    context_object_name = 'recipe_list'

    def get_queryset(self):
        return models.Recipe.objects.all()

class RecipeDetailView(generic.DetailView):
    model = models.Recipe
    template_name = 'food/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = models.Ingredient.objects.filter(recipe=self.object)
        return context

class RecipeCreateView(generic.edit.CreateView):
    model = models.Recipe
    form_class = forms.RecipeForm
    context_object_name = 'recipes'
    template_name = 'food/recipe_create.html'
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        return super(RecipeCreateView, self).form_valid(form=form)

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})

class IngredientCreateView(generic.edit.CreateView):
    model = models.Ingredient
    form_class = forms.IngredientForm
    template_name = 'food/ingredient_create.html'
    context_object_name = 'ingredients'
    success_url = reverse_lazy('recipe_detail')

    def form_valid(self, form):
        return super(IngredientCreateView, self).form_valid(form=form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = models.Recipe.objects.get(pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.kwargs['pk']})


class RecipeDeleteView(generic.edit.DeleteView):
    model = models.Recipe
    template_name = 'food/delete_recipe.html'
    success_url = reverse_lazy('recipe_list')
