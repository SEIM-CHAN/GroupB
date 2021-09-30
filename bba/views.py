from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django import template
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment, Thread
from .forms import ThreadForm, CommentForm, CommentUpdateForm 

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
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        return user

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
    
class ThreadDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Thread
    template_name = 'bba/thread_delete.html'
    success_url = reverse_lazy('bba:thread')

    def form_valid(self, form):
        return super().form_valid(form)

class CommentListView(generic.ListView):
    model = Thread
    template_name = 'bba/comment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'thread': Thread.objects.filter(id=self.kwargs['pk']).first(),
        })
        return context

    def get_queryset(self):
        comments = Comment.objects.filter(thread_id=self.kwargs['pk']).order_by('-created_at')
        return comments
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        return user

class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'bba/comment_create.html'

    # def get_return_link(request):
    #     # top_page = resolve_url('diary:top')  # 最新の日記一覧
    #     referer = request.environ.get('HTTP_REFERER')  # これが、前ページのURL
    #     return refer
    def get_success_url(self):
        return reverse_lazy('bba:comment', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.thread = Thread.objects.filter(id=self.kwargs['pk']).first()
        object.save()
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    form_class = CommentUpdateForm
    template_name = 'bba/comment_update.html'

    def get_success_url(self):
        comment_id =Comment.objects.filter(id=self.kwargs['pk']).first()
        thread_id = Thread.objects.filter(subject=comment_id.thread).first()
        return reverse_lazy('bba:comment', kwargs={'pk': thread_id.id})
    
    def form_valid(self, form):
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    template_name = 'bba/comment_delete.html'

    def get_success_url(self):
        comment_id =Comment.objects.filter(id=self.kwargs['pk']).first()
        thread_id = Thread.objects.filter(subject=comment_id.thread).first()
        return reverse_lazy('bba:comment', kwargs={'pk': thread_id.id})
    
    