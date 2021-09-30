from django.urls import reverse_lazy, reverse
from .models import Thread, Comment
from .forms import ThreadCreateForm, CommentCreateForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.

class IndexViews(generic.TemplateView):
    template_name = "index.html"


class ThreadListView(LoginRequiredMixin, generic.ListView):
    model = Thread    # Thread.objects.all()を裏側でやってくれてる
    template_name = "thread_list.html"
    context_object_name = "threadList"

    def get_queryset(self):
        threads = Thread.objects.all().order_by('-created_at')
        return threads


class ThreadCreateView(LoginRequiredMixin, generic.CreateView):
    model = Thread
    template_name = 'thread_create.html'
    form_class = ThreadCreateForm
    success_url = reverse_lazy('ichan:thread_list')

    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.user = self.request.user
        thread.save()
        messages.success(self.request, 'スレッドを作成しました')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'スレッドの作成に失敗しました')
        return super().form_invalid(form)
    
    
class ThreadDetailView(LoginRequiredMixin, generic.DetailView):
    model = Thread
    template_name = 'thread_detail.html'


class CommentListView(generic.ListView):
    template_name = 'comment/comment_list.html'
    context_object_name = 'comment'
    model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'thread': Thread.objects.filter(id=self.kwargs['pk']).first(),
        })
        return context

    def get_queryset(self):
        comments = Comment.objects.filter(thread=self.kwargs['pk']).order_by('created_at')
        return comments

class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    """"コメント作成"""
    template_name = 'comment/comment_create.html'
    model = Comment
    form_class = CommentCreateForm

    def get_success_url(self):
        return reverse_lazy('ichan:comment_list', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.user = self.request.user
        thread.thread = Thread.objects.filter(id=self.kwargs['pk']).first()
        thread.save()
        messages.success(self.request,'コメントを作成しました。')
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request,'コメントの作成に失敗しました。')
        return super().form_invalid(form)

class ThreadDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Thread
    template_name = 'thread_delete.html'
    success_url = reverse_lazy('ichan:thread_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "スレッドを削除しました。")
        return super().delete(request, *args, **kwargs)

