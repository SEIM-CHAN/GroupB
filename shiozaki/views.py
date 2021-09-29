from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic

from django.contrib import messages

from .models import Thread, Comment

from .forms import BoardCreateForm, CommentCreateForm

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ShiozakiView(generic.ListView):
    model = Thread
    template_name = 'shiozaki/index.html'

    def get_queryset(self):
        threads = Thread.objects.all().order_by('created_at').reverse()
        return threads

#一覧
class BoardListView(generic.ListView):
    model = Thread
    template_name = 'shiozaki/board_list.html'
    paginate_by = 2

    def get_queryset(self):
        threads = Thread.objects.all().order_by('created_at').reverse()
        return threads

#一覧
class YourBoardsListView(generic.ListView):
    model = Thread
    template_name = 'shiozaki/board_list.html'
    paginate_by = 2

    def get_queryset(self):
        threads = Thread.objects.filter(user=self.request.user).order_by('created_at').reverse()
        return threads

#掲示板詳細
class BoardDetailView(generic.DetailView):
    model = Thread
    template_name = 'shiozaki/board_detail.html'

#掲示板作成
class BoardCreateView(LoginRequiredMixin, generic.CreateView):
    model = Thread
    template_name = 'shiozaki/board_create.html'
    form_class = BoardCreateForm
    success_url = reverse_lazy('shiozaki:board-list')

    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.user = self.request.user
        thread.save()
        messages.success(self.request, "掲示板を作成しました。")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "掲示板の作成に失敗しました。")
        return super().form_invalid(form)

#掲示板更新
class BoardUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Thread
    template_name = 'shiozaki/board_update.html'
    form_class = BoardCreateForm

    def get_success_url(self):
        return reverse_lazy('shiozaki:board-detail', kwargs={'pk': self.kwargs['pk']})
    
    def form_valid(self, form):
        messages.success(self.request, "掲示板を更新しました。")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "掲示板の更新に失敗しました。")
        return super().form_invalid(form)

#掲示板削除
class BoardDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Thread
    template_name = 'shiozaki/board_delete.html'
    success_url = reverse_lazy('shiozaki:board-list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "掲示板を削除しました。")
        return super().delete(request, *args, **kwargs)


#コメント作成
class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    template_name = 'shiozaki/comment_create.html'
    form_class = CommentCreateForm

    def get_success_url(self):
        return reverse_lazy('shiozaki:board-detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        print(self.kwargs['pk'])

        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.title = self.kwargs['pk']
        comment.save()

        Thread.addComments(Thread, comment)

        messages.success(self.request, "コメントを送信しました。")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "コメントの送信に失敗しました。")
        return super().form_invalid(form)

# #コメント更新
# class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = Comment
#     template_name = 'shiozaki/board_update.html'
#     form_class = CommentCreateForm

#     def get_success_url(self):
#         return reverse_lazy('shiozaki:board-detail', kwargs={'pk': self.kwargs['pk']})
    
#     def form_valid(self, form):
#         messages.success(self.request, "コメントを更新しました。")
#         return super().form_valid(form)
    
#     def form_invalid(self, form):
#         messages.error(self.request, "コメントの更新に失敗しました。")
#         return super().form_invalid(form)

# #コメント削除
# class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = Comment
#     template_name = 'shiozaki/board_delete.html'
#     success_url = reverse_lazy('shiozaki:board-detail')

#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, "コメントを削除しました。")
#         return super().delete(request, *args, **kwargs)