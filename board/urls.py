
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('',views.IndexViews.as_view(),name="index"),
    path('board-list/',views.BoardListView.as_view(),name="board_list"),
    path('board-detail/<int:pk>/',views.BoardDetailView.as_view(),name="board_detail"),
    path('board-create/',views.BoardCreateView.as_view(),name="board_create"),
    path('coment-create/<int:pk>/',views.ComentCreateView.as_view(),name="coment_create"),
    path('board-updata/<int:pk>/',views.BoardUpdateView.as_view(),name="board_update"),
    path('board-delete/<int:pk>/',views.BoardDeleteView.as_view(),name="board_delete"),
    path('coment-updata/<int:pk>/',views.ComentUpdateView.as_view(),name="coment_update"),
    path('coment-delete/<int:pk>/',views.ComentDeleteView.as_view(),name="coment_delete"),
]
