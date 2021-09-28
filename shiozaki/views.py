from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic

from django.contrib import messages

from .models import Thread

from .forms import BoardCreateForm

from .models import Thread

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ShiozakiView(generic.TemplateView):
    template_name = 'shiozaki/index.html'

class BoardListView(generic.TemplateView):
    model = Thread
    template_name = 'shiozaki/board_list.html'
    paginate_by = 2

    def get_queryset(self):
        threads = Thread.objects.filter(user=self.request.user).order_by('created-at')
        return threads

class BoardDetailView(generic.TemplateView):
    model = Thread
    template_name = 'shiozaki/board_detail.html'

class BoardCreateView(generic.CreateView):
    model = Thread
    template_name = 'shiozaki/board_create.html'
    form_class = BoardCreateForm

#更新
class BoardUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Thread
    template_name = 'shiozaki/board_update.html'
    form_class = BoardCreateForm

    def get_success_url(self):
        return reverse_lazy('board-detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        messages.success(self.request, "掲示板を更新しました。")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "掲示板の更新に失敗しました。")
        return super().form_invalid(form)

#削除
class BoardDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Thread
    template_name = 'shiozaki/board_delete.html'
    success_url = reverse_lazy('board-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "掲示板を削除しました。")
        return super().delete(request, *args, **kwargs)
