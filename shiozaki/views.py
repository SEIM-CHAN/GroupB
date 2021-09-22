from django.shortcuts import render
from django.views import generic

from django.contrib import messages

from .forms import InquiryForm

# Create your views here.
class ShiozakiView(generic.TemplateView):
    template_name = 'shiozaki/index.html'

class InquiryView(generic.FormView):
    template_name = 'shiozaki/inquiry.html'
    form_class = InquiryForm