from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from . import forms

# Create your views here.
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "account/home.html"

class LoginView(LoginView):
    """Login Page"""
    form_class = forms.LoginForm
    template_name = "account/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    """Logout Page"""
    template_name = "account/login.html"

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    """Change password"""
    success_url = reverse_lazy("account:password_change_done")
    template_name = "account/password_change.html"

class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    """Done changed password"""
    template_name = "account/password_change_done.html"
