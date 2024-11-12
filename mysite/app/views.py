import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView

from . import forms, models

logger = logging.getLogger(__name__)


class SeversMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servers"] = models.Server.objects.filter(
            Q(owner=self.request.user) | Q(members=self.request.user)
        ).distinct()
        if "server_pk" in self.kwargs:
            context["current_server"] = models.Server.objects.get(
                pk=self.kwargs["server_pk"]
            )
        return context


class IndexView(LoginRequiredMixin, SeversMixin, TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ServerCreateView(LoginRequiredMixin, SeversMixin, CreateView):
    model = models.Server
    form_class = forms.ServerCreateForm
    template_name = "app/server_create.html"
    success_url = reverse_lazy("app:index")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ServerDetailView(LoginRequiredMixin, SeversMixin, DetailView):
    model = models.Server
    template_name = "app/server_detail.html"
    pk_url_kwarg = "server_pk"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["role_form"] = forms.RoleForm()
        context["server_members_form"] = forms.ServerMembersForm()
        return context


class MessageView(TemplateView):
    template_name = "app/message.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = {
            "content": "BLAH, asdlkfjasdfkjasdfljasdf;lkjasdfjkasdf;jasdf;jkasdf;jkasdf;lkjasdf;lkj"
        }

        return context
