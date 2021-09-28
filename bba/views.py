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
    model = Comment
    template_name = 'bba/comment.html'

#     def get_queryset(self):
#         comment_list = Comment.objects.all()
#         return super().get_queryset()

# class CommentCreateView(generic.CreateView):
#     pass