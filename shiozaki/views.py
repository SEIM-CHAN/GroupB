from django.shortcuts import render
from django.views import generic

# Create your views here.
class ShiozakiView(generic.TemplateView):
    template_name = 'shiozaki.html'