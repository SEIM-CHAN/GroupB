from django.http import request
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect

from .models import NiceThread, NiceComment
from .forms import NiceThreadCreateForm, NiceCommentCreateForm, NiceCommentUpdateForm

"""tools
"""
class Verification():
    """検証用クラス"""
    def verificationThreadUser(self, id = None):
        """リクエストユーザーとスレッドユーザーの検証"""
        if id is None:
            id = self.kwargs['pk']
        target = NiceThread.objects.filter(id=id).first()
        return (not target is None) and (target.user.id == self.request.user.id)
    
    def verificationCommentUser(self, id = None):
        """リクエストユーザーとコメントユーザーの検証"""
        if id is None:
            id = self.kwargs['pk']
        target = NiceComment.objects.filter(id=id).first()
        return (not target is None) and ((not target.user is None) and (target.user.id == self.request.user.id))


"""Common Views
"""
class IndexView(generic.TemplateView):
    """トップ"""
    template_name = 'nice_board/index.html'

"""Thread View
"""
class NiceThreadListView(generic.ListView):
    """スレッドリスト"""
    template_name = 'nice_board/threads/list.html'
    model = NiceThread
    
    def get_queryset(self):
        threds = NiceThread.objects.order_by('-created_at')
        return threds

class NiceThreadManageView(LoginRequiredMixin, NiceThreadListView):
    """スレッド管理"""
    template_name = 'nice_board/threads/manage.html'
    
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


class NiceThreadUpdateView(LoginRequiredMixin, generic.UpdateView, Verification):
    """スレッド編集"""
    template_name = 'nice_board/threads/update.html'
    model = NiceThread
    form_class = NiceThreadCreateForm

    def get(self, request, *args, **kwargs):
        if super().verificationThreadUser():
            return super().get(request, *args, **kwargs)
        else:
            return redirect('nice_board:index')

    def form_valid(self, form):
        if super().verificationThreadUser():
            messages.success(self.request, 'スレッドを変更しました')
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
            
    def form_invalid(self, form):
        messages.error(self.request, 'スレッドの変更に失敗しました')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('nice_board:threads')

class NiceThreadDeleteView(LoginRequiredMixin, generic.DeleteView, Verification):
    """スレッド削除"""
    template_name = 'nice_board/threads/delete.html'
    model = NiceThread
    success_url = reverse_lazy('nice_board:threads')

    def get(self, request, *args, **kwargs):
        if super().verificationThreadUser():
            return super().get(request, *args, **kwargs)
        else:
            return redirect('nice_board:index')

    def delete(self, *args, **kwargs):
        if super().verificationThreadUser():
            messages.success(self.request, "スレッドを削除しました")
            return super().delete(request, *args, **kwargs)
        else:
            return redirect('nice_board:index')

"""Comment View
"""
class NiceCommentListView(generic.ListView):
    """コメント一覧"""
    template_name = 'nice_board/comments/list.html'
    context_object_name = 'comments'
    model = NiceComment

    def get_context_data(self, **kwargs):
        """スレッド番号"""
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
        """スレッド番号添付"""
        context = super().get_context_data(**kwargs)
        context.update({
            'pk': self.kwargs['pk'],
            })
        return context

    def form_valid(self, form):
        """投稿ユーザー判定"""
        comment = form.save(commit=False)
        if(self.request.user.is_anonymous):
            comment.user = None
        else:
            comment.user =  self.request.user
        comment.nice_thread = NiceThread.objects.filter(id=self.kwargs['pk']).first()
        comment.save()
        messages.success(self.request, 'スレッドを作成しました')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'スレッドの作成に失敗しました')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('nice_board:comments', kwargs={'pk': self.kwargs['pk']})

class NiceCommentCreateToolView(NiceCommentCreateView):
    """コメント作成ループ"""
    def get_success_url(self):
        return reverse('nice_board:comment_create_tool', kwargs={'pk': self.kwargs['pk']})


class NiceCommentUpdateView(LoginRequiredMixin, generic.UpdateView, Verification):
    """コメント削除"""
    template_name = 'nice_board/comments/update.html'
    model = NiceComment
    form_class = NiceCommentCreateForm
    pk_url_kwarg = 'pk2'

    def get(self, request, *args, **kwargs):
        if super().verificationThreadUser(self.kwargs['pk']) or super().verificationCommentUser(self.kwargs['pk2']):
            return super().get(request, *args, **kwargs)
        else:
            return redirect('nice_board:index')

    def get_context_data(self, **kwargs):
        """スレッド番号添付"""
        context = super().get_context_data(**kwargs)
        context.update({
            'pk': self.kwargs['pk'],
            })
        return context
    
    def form_valid(self, form):
        pageAdmin = super().verificationThreadUser(self.kwargs['pk'])
        sameUser = super().verificationCommentUser(self.kwargs['pk2'])
        if pageAdmin or sameUser:
            comment = form.save(commit=False)
            comment.user = None
            if pageAdmin and (not sameUser):
                text = "コメントは管理者によって削除されました"
            else:
                text = "コメントは削除されました"
            comment.text = text
            comment.save()
            messages.success(self.request, 'コメントを削除しました')
            return super().form_valid(form)
        else:
            return redirect('nice_board:index')
    def form_invalid(self, form):
        messages.success(self.request, 'コメントの削除に失敗しました')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('nice_board:threads')