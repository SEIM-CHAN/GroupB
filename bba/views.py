from django.shortcuts import render
from django.views import generic
from .models import Thread

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "bba/base.html"

class ThreadView(generic.ListView):
    model = Thread
    template_name = 'bba/thread.html'

# class ThreadView(generic.TemplateView):
#     template_name = "bba/thread.html"