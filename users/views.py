
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import models, forms

class RegistrationView(CreateView):
    form_class = forms.RegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('users:login')

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('users:user_list')

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')

class UserListView(ListView):
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    model = models.User

    def get_queryset(self):
        return models.User.objects.all()