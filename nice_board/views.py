from django.http import request
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .models import NiceThread, NiceComment
from .forms import NiceThreadCreateForm, NiceCommentCreateForm

class IndexView(generic.TemplateView):
    """トップ"""
    template_name = 'nice_board/index.html'

class NiceThreadListView(generic.ListView):
    """スレッドリスト"""
    template_name = 'nice_board/threads/list.html'
    model = NiceThread
    
    def get_queryset(self):
        threds = NiceThread.objects.order_by('-created_at')
        return threds

class NiceThreadManageView(LoginRequiredMixin, generic.ListView):
    """スレッド管理"""
    template_name = 'nice_board/threads/manage.html'
    model = NiceThread
    
    def get_queryset(self):
        threds = NiceThread.objects.filter(user=self.request.user).order_by('-created_at')
        return threds

class NiceThreadCreateView(LoginRequiredMixin,generic.CreateView):
    """"スレッド作成"""
    template_name = 'nice_board/threads/create.html'
    model = NiceThread
    form_class = NiceThreadCreateForm
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
    """スレッド編集"""
    template_name = 'nice_board/threads/update.html'
    model = NiceThread
    form_class = NiceThreadCreateForm
    def get_success_url(self):
        return reverse_lazy('nice_board:threads')
    def form_valid(self, form):
        messages.success(self.request, 'スレッドを変更しました')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'スレッドの変更に失敗しました')
        return super().form_invalid(form)

class NiceThreadDeleteView(LoginRequiredMixin, generic.DeleteView):
    """スレッド削除"""
    template_name = 'nice_board/threads/delete.html'
    model = NiceThread
    success_url = reverse_lazy('nice_board:threads')
    def delete(self, *args, **kwargs):
        messages.success(self.request, "スレッドを削除しました")
        return super().delete(request, *args, **kwargs)


class NiceCommentListView(generic.ListView):
    """コメント一覧"""
    template_name = 'nice_board/comments/list.html'
    context_object_name = 'comments'
    model = NiceComment
    def get_context_data(self, **kwargs):
       context = super(NiceCommentListView, self).get_context_data(**kwargs)
       context.update({
           'thread': NiceThread.objects.filter(id=self.kwargs['pk']).first(),
       })
       return context
    def get_queryset(self):
        comments = NiceComment.objects.filter(nice_thread_id=self.kwargs['pk']).order_by('created_at')
        return comments

class NiceCommentCreateView(generic.CreateView):
    """"コメント作成"""
    template_name = 'nice_board/comments/create.html'
    model = NiceComment
    form_class = NiceCommentCreateForm
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context.update({
           'pk': self.kwargs['pk'],
       })
       return context
    def form_valid(self, form):
        comment = form.save(commit=False)
        if(self.request.user is None):
            comment.user = None
        else:
            comment.user =  self.request.user
        comment.nice_thread = NiceThread.objects.filter(id=self.kwargs['pk']).first()
        print("save")
        comment.save()
        messages.success(self.request, 'スレッドを作成しました')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'スレッドの作成に失敗しました')
        return super().form_invalid(form)

    def get_success_url(self):
        if(self.kwargs['none'] == 'none'):
            return reverse('nice_board:create_tool', kwargs={'pk': self.kwargs['pk']}) 
        return reverse('nice_board:comments', kwargs={'pk': self.kwargs['pk']})
class NiceCommentCreateToolView(NiceCommentCreateView):
    def get_success_url(self):
        return reverse('nice_board:comment_create_tool', kwargs={'pk': self.kwargs['pk']}) 