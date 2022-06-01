from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import CreationForm
from .forms import ChangePasswordForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:main')
    template_name = 'users/signup.html'


class PasswordChangeView(UpdateView):
    form_class = ChangePasswordForm
    success_url = reverse_lazy('users:done')
    template_name = 'users/password_change.html'
