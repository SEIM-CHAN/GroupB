from django.shortcuts import render
from django.views import generic

# Create your views here.
class KimizukaView(generic.TemplateView):
    template_name = "kimizuka.html"