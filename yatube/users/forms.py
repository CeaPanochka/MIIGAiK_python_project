from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Contact


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'body')


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(label='Текущий пароль')
    new_password = forms.CharField(label='Новый пароль')
    repeat_new_password = forms.CharField(label='Повтор нового пароля')
