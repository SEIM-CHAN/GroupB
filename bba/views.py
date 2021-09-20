from django.shortcuts import render
from django.views import generic
from django.views import LoginRequiredMixin

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "bba/base.html"

class BbaListView(LoginRequiredMixin, generic.ListView):
    pass