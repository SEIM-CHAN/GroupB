from django.urls import path, include
from django.contrib.staticfiles.urls import static
from . import views
from config import settings

#config/urls.pyにて、path('', include('shiozaki.urls')),を追加
app_name = 'shiozaki'
urlpatterns = [
    path('', views.ShiozakiView.as_view(), name='index'),
    path('board-list/', views.BoardListView.as_view(), name='board-list'),
    path('your-boards/', views.YourBoardsListView.as_view(), name='your-board'),

    #掲示板
    path('board-detail/<int:pk>/', views.BoardDetailView.as_view(), name='board-detail'),
    path('board-create/', views.BoardCreateView.as_view(), name='board-create'),
    path('board-update/<int:pk>/', views.BoardUpdateView.as_view(), name='board-update'),
    path('board-delete/<int:pk>/', views.BoardDeleteView.as_view(), name='board-delete'),

    #コメント
    path('comment-create/<int:pk>/', views.CommentCreateView.as_view(), name='comment-create'),
    # path('comment-update/<int:bk>/<int:pk>/', views.CommentUpdateView.as_view(), name='comment-update'),
    # path('comment-delete/<int:bk>/<int:pk>/', views.CommentDeleteView.as_view(), name='comment-delete'),

    #認証機能
    path('accounts/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
