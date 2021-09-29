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
    ordering = "-created_at"

    def get_queryset(self):
        threads = Thread.objects.all().order_by('-created_at')
        return threads


class ThreadCreateView(LoginRequiredMixin, generic.CreateView):
    model = Thread
    template_name = 'thread_create.html'
    form_class = ThreadCreateForm
    success_url = reverse_lazy('thread_list')

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
        context = super(CommentListView, self).get_context_data(**kwargs)
        context.update({
            'thread': Thread.objects.filter(id=self.kwargs['pk']).first(),
        })
        return context

    def get_queryset(self):
        comments = Comment.objects.filter(thread_id=self.kwargs['pk']).order_by('created_at')
        return comments

class CommentCreateView(generic.CreateView):
    """"コメント作成"""
    template_name = 'comments/comment_create.html'
    model = Comment
    form_class = CommentCreateForm

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
            
        if comment.text == "":
            return self.form_invalid(form)
            
        comment.nice_thread = Thread.objects.filter(id=self.kwargs['pk']).first()
        comment.save()
        messages.success(self.request, 'スレッドを作成しました')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'スレッドの作成に失敗しました')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('comments', kwargs={'pk': self.kwargs['pk']})

class CommentCreateToolView(CommentCreateView):
    """コメント作成ループ"""
    def get_success_url(self):
        return reverse('comment_create_tool', kwargs={'pk': self.kwargs['pk']})





# def post_list(request, pk):
#     per_page = 10

#     thread = get_object_or_404(Thread,pk=pk)
#     post_list= Post.objects.filter(thread=thread)
#     form = PostForm(request.POST or None)

#     if form.is_valid():
#         post = form.save(commit=False)
#         post.thread = thread
#         post.save()
#         return redirect('ichan:post', pk=thread.pk)

#     context = {'form': form, 'post_list': post_list}
#     return render(request, 'post.html', context)
