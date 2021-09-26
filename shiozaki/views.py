from django.shortcuts import render
from django.views import generic

from django.contrib import messages

from .models import Thread

from .forms import BoardCreateForm

#from .models import Thread

# Create your views here.
class ShiozakiView(generic.TemplateView):
    template_name = 'shiozaki/index.html'

class BoardListView(generic.TemplateView):
    model = Thread
    template_name = 'shiozaki/board_list.html'

class BoardDetailView(generic.TemplateView):
    model = Thread
    template_name = 'shiozaki/board_detail.html'

class BoardCreateView(generic.CreateView):
    model = Thread
    template_name = 'shiozaki/board_create.html'
    form_class = BoardCreateForm

class BoardUpdateView(generic.UpdateView):
    model = Thread
    template_name = 'shiozaki/board_update.html'
    form_class = BoardCreateForm