from django.urls import path
from . import views

app_name = 'nice_board'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('threads', views.NiceThreadListView.as_view(), name='threads'),
    path('thread/manage', views.NiceThreadManageView.as_view(), name='thread_manage'),
    path('thread/create', views.NiceThreadCreateView.as_view(), name='thread_create'),
    path('thread/update/<int:pk>', views.NiceThreadUpdateView.as_view(), name='thread_update'),
    path('thread/delete/<int:pk>', views.NiceThreadDeleteView.as_view(), name='thread_delete'),
    path('<int:pk>/', views.NiceCommentListView.as_view(), name='comments'),
    path('<int:pk>/create', views.NiceCommentCreateView.as_view(), name='comment_create'),
    path('<int:pk>/create/tool', views.NiceCommentCreateToolView.as_view(), name='comment_create_tool'),
]