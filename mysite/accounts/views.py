import logging

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from . import forms

logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = "accounts/index.html"


class RegisterUser(CreateView):
    model = User
    form_class = forms.RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        form.full_clean()
        # Saves the form
        return super().form_valid(form)


class LoginUser(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"
    next_page = reverse_lazy("app:dashboard")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("app:dashboard"))
        return super().get(request, *args, **kwargs)


class LogoutUser(LogoutView):
    next_page = reverse_lazy("accounts:index")
