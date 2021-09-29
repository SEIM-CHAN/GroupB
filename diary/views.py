import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import InquiryForm, DiaryThreadsForm ,DiaryCommentsForm
from .models import Threads,Comments

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(generic.ListView):
    model = Threads
    template_name = 'diary_list.html'
    paginate_by = 5

    # def get_queryset(self):
    #     diaries = Threads.objects.filter(user=self.request.user).order_by('-pub_date')
    #     return diaries
    def get_queryset(self):
        threads = Threads.objects.order_by('-pub_date')
        return threads

class DiaryDetailView(generic.ListView):
    model = Comments
    template_name = 'diary_detail.html'
    paginate_by = 20

    # def get_queryset(self):
    #     diaries = Threads.objects.filter(user=self.request.user).order_by('-pub_date')
    #     return diaries
    def get_queryset(self):
        comments = Comments.objects.filter(thread_id=self.kwargs['pk']).order_by('-pub_date')
        return comments

class DiaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Threads
    template_name = 'diary_create.html'
    form_class = DiaryThreadsForm
    success_url = reverse_lazy('diary:diary_list')

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.user = self.request.user
        diary.save()
        messages.success(self.request, '日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)

class CommentsCreateView(generic.CreateView):
    model = Comments
    template_name = 'diary_update.html'
    form_class = DiaryCommentsForm

    def get_success_url(self):
        return reverse_lazy('diary:diary_update', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        diary = form.save(commit=False)
        diary.thread = Threads.objects.filter(id=self.kwargs['pk']).first()
        diary.save()
        messages.success(self.request, 'コメントしました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "コメントに失敗しました。")
        return super().form_invalid(form)

class DiaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Threads
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('diary:diary_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "日記を削除しました。")
        return super().delete(request, *args, **kwargs)
