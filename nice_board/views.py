from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import NiceThread
from .forms import NiceThreadNewForm

class IndexView(generic.TemplateView):
    template_name = 'nice_board/index.html'

# self.kwargs['pk']
class NiceThreadListView(generic.ListView):
    template_name = 'nice_board/threads/list.html'
    model = NiceThread
    
    def get_queryset(self):
        threds = NiceThread.objects.order_by('-created_at')
        return threds

class NiceThreadNewView(LoginRequiredMixin,generic.CreateView):
    template_name = 'nice_board/threads/new.html'
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

class NiceCommentListView(generic.TemplateView):
    template_name = 'nice_board/comments/list.html'