from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms
from django.views import generic


class TodoListView(generic.ListView):
    template_name = 'todo/todo_list.html'
    context_object_name = 'ToDo_list'

    def get_queryset(self):
        return models.TodoModel.objects.all()


class CreateTodoView(generic.CreateView):
    template_name = 'todo/create_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTodoView, self).form_valid(form=form)


class DeleteTodoView(generic.DeleteView):
    template_name = 'todo/confirm_delete.html'
    success_url = '/todo_list/'

    def get_object(self, *args, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)

class UpdateTodoView(generic.UpdateView):
    template_name = 'todo/update_todo.html'
    form_class = forms.TodoForm
    success_url = '/todo_list/'

    def get_object(self, *args, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)

