from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django import template
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment, Thread
from .forms import ThreadForm, CommentForm

register = template.Library()

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_list = Comment.objects.filter(thread=self.kwargs['pk'])
        context['greenhouse_data_list'] = comment_list
        return context

class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'bba/comment_create.html'
    success_url = reverse_lazy('bba:thread')

    # def get_return_link(request):
    #     # top_page = resolve_url('diary:top')  # 最新の日記一覧
    #     referer = request.environ.get('HTTP_REFERER')  # これが、前ページのURL
    #     return refer


    def form_valid(self, form):
        thread = form.save(commit=False)
        thread.user = self.request.user
        thread.save()
        return super().form_valid(form)

    # def get_success_url(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return reverse('bba:comment', kwargs={'pk': self.kwargs['pk']})