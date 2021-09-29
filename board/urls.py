
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('',views.BoardView.as_view(),name="board"),
    path('board-list/',views.BoardListView.as_view(),name="board_list"),
    path('board-detail/<int:pk>/',views.BoardDetailView.as_view(),name="board_detail"),
    path('board-create/',views.BoardCreateView.as_view(),name="board_create"),
    path('coment-create/<int:pk>/',views.ComentCreateView.as_view(),name="coment_create"),
]
