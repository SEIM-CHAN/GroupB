from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Board
from .models import Coment
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.

class BoardView(generic.TemplateView):
    template_name = "board/index.html"

class BoardListView(LoginRequiredMixin,generic.ListView):
    model = Board
    template_name = 'board_list.html'

    def get_queryset(self):
        boards = Board.objects.all().order_by('-created_at')
        return boards

class BoardDetailView(LoginRequiredMixin,generic.ListView):
    model = Coment
    template_name = 'board/board_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(BoardDetailView, self).get_context_data(**kwargs)
        context.update({
            'board': Board.objects.filter(id=self.kwargs['pk']).first(),
        })
        return context

    def get_queryset(self):
        coments = Coment.objects.filter(board_id=self.kwargs['pk']).order_by('-created_at')
        return coments


    


from .forms import BoardCreateForm


class BoardCreateView(LoginRequiredMixin,generic.CreateView):
    model = Board
    template_name = 'board/board_create.html'
    form_class = BoardCreateForm
    success_url = reverse_lazy('board:board_list')

    def form_valid(self, form):
        board = form.save(commit=False)
        board.user = self.request.user
        board.save()
        messages.success(self.request,'スレッドを作成しました。')
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request,'スレッドの作成に失敗しました。')
        return super().form_invalid(form)

from .forms import ComentCreateForm
from django.urls import reverse
class ComentCreateView(LoginRequiredMixin,generic.CreateView):
    model = Coment
    template_name = 'board/coment_create.html'
    form_class = ComentCreateForm
    success_url = reverse_lazy('board:board_detail')

    def get_success_url(self):
        return reverse('board:board_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        board = form.save(commit=False)
        board.user = self.request.user
        board.board = Board.objects.filter(id=self.kwargs['pk']).first()
        board.save()
        messages.success(self.request,'コメントを作成しました。')
        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request,'コメントの作成に失敗しました。')
        return super().form_invalid(form)





