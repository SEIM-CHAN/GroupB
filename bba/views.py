from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Thread

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "bba/base.html"

# class ThreadView(LoginRequiredMixin ,generic.ListView):
#     # model = Thread
#     template_name = 'bba/thread.html'

class ThreadView(generic.TemplateView):
    template_name = "bba/thread.html"