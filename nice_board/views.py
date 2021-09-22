from django.http import request
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import NiceComments, NiceThread
from .forms import NiceThreadNewForm

class IndexView(generic.TemplateView):
    template_name = 'nice_board/index.html'

class NiceThreadListView(generic.ListView):
    template_name = 'nice_board/threads/list.html'
    model = NiceThread
    
    def get_queryset(self):
        threds = NiceThread.objects.order_by('-created_at')
        return threds

class NiceThreadCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = 'nice_board/threads/create.html'
    model = NiceThread
    form_class = NiceThreadNewForm
    success_url = reverse_lazy('nice_board:threads')
    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.user = self.request.user
        thread.save()
        messages.success(self.request, 'スレッドを作成しました')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'スレッドの作成に失敗しました')
        return super().form_invalid(form)

class NiceThreadUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'nice_board/threads/update.html'
    model = NiceThread
    form_class = NiceThreadNewForm
    def get_success_url(self):
        return reverse_lazy('nice_board:threads')
    def form_valid(self, form):
        messages.success(self.request, 'スレッドを変更しました')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'スレッドの変更に失敗しました')
        return super().form_invalid(form)

class NiceThreadDeleteView(generic.DeleteView):
    template_name = 'nice_board/threads/delete.html'
    model = NiceThread
    success_url = reverse_lazy('nice_board:threads')
    def delete(self, *args, **kwargs):
        messages.success(self.request, "スレッドを削除しました")
        return super().delete(request, *args, **kwargs)


class NiceCommentListView(generic.ListView):
    template_name = 'nice_board/comments/list.html'
    model = NiceComments

    def get_queryset(self):
        comments = NiceComments.objects.filter(nice_thread_id=self.kwargs['pk']).order_by('created_at')
        return comments
