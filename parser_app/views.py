from django.shortcuts import render, redirect
from django.views import generic
from . import models, forms

class LitrezListView(generic.ListView):
    template_name = 'parser_app/litrez_list.html'
    context_object_name = 'litrez'
    model = models.LitrezModel

    def get_queryset(self):
        return models.LitrezModel.objects.all()

class RezkaListView(generic.ListView):
    template_name = 'parser_app/rezka_list.html'
    context_object_name = 'rezka'
    model = models.RezkaModel

    def get_queryset(self):
        return models.RezkaModel.objects.all()

class ParserFormView(generic.FormView):
    template_name = 'parser_app/litrez_form.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            method = form.cleaned_data['method']
            form.parser_data()

            if method == 'litrez.ru':
                return redirect('litrez_list')
            elif method == 'rezka.ag':
                return redirect('rezka_list')

        return self.form_invalid(form)
