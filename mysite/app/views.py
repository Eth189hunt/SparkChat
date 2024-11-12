from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from . import forms, models


class IndexView(TemplateView):
    template_name = "app/index.html"

class MessageView(TemplateView):
    template_name = "app/message.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["message"] = {"content": "BLAH, asdlkfjasdfkjasdfljasdf;lkjasdfjkasdf;jasdf;jkasdf;jkasdf;lkjasdf;lkj"}

        return context
