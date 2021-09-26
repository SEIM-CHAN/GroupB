from django.urls import path
from . import views

#config/urls.pyにて、path('', include('shiozaki.urls')),を追加
urlpatterns = [
    path('', views.ShiozakiView.as_view(), name='index'),
    path('board-list/', views.BoardListView.as_view(), name='board-list'),
    path('board-detail/', views.BoardDetailView.as_view(), name='board-detail'),
    path('board-create/', views.BoardCreateView.as_view(), name='board-create'),
    path('board-update/', views.BoardUpdateView.as_view(), name='board-update'),
]
