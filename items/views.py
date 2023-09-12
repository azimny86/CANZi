from django.shortcuts import render
from django.views import generic
from .models import Items


class IndexView(generic.TemplateView):
    template_name = 'index.html'
