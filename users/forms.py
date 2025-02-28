from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Введите Email')
    age = forms.IntegerField(required=True, label='Укажите ваш возраст')
    phone = forms.CharField(required=True, label='Введите номер телефона')
    whats_phone = forms.CharField(required=True, label='Введите ваш WhatsApp номер')
    experience = forms.IntegerField(required=True, label='Укажите ваш опыт')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Укажите пол')

    class Meta:
        model = models.CustomUser
        fields = ('username',
                  'email',
                  'password1',
                  'password2','first_name',
                  'last_name' ,
                  'age',
                  'phone',
                  'whats_phone',
                  'experience',
                  'gender')
        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.phone = self.cleaned_data['phone']
            user.experience = self.cleaned_data['experience']
            user.gender = self.cleaned_data['gender']

            if commit:
                user.save()
            return user
