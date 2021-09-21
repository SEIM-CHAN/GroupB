from re import template
from django.shortcuts import render
from django.views import generic
# Create your views here.

class IndexViews(generic.TemplateView):
    template_name = "index.html"