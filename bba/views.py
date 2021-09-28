from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment, Thread
from .forms import ThreadForm

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "bba/base.html"

class ThreadListView(generic.ListView):
    model = Thread
    template_name = 'bba/thread.html'

    def get_queryset(self):
        thread_list = Thread.objects.all().order_by('created_at') 
        return thread_list

class ThreadCreateView(LoginRequiredMixin, generic.CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'bba/thread_create.html'
    success_url = reverse_lazy('bba:thread')

    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.user = self.request.user
        thread.save()
        return super().form_valid(form)
    
class CommentListView(generic.ListView):
    model = Thread
    template_name = 'bba/comment.html'

    #CommentモデルのthreadとTreadモデルのsubjectが一致したものを表示
    def get_context_data(self, **kwargs):
        # comment_list = Comment.objects.all()
        context = super().get_context_data(**kwargs)
        comment_list = Comment.objects.filter(thread=self.kwargs['pk'])
        context['greenhouse_data_list'] = comment_list
        return context

# class CommentCreateView(generic.CreateView):
#     pass