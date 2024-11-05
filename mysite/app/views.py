from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from . import forms, models


class IndexView(TemplateView):
    template_name = "app/index.html"
