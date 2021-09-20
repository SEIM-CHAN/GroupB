from django.urls import path
from . import views

app_name = 'nice_board'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('threads', views.NiceThreadListView.as_view(), name='threads'),
    path('thread/new', views.NiceThreadNewView.as_view(), name='thread_new'),
    path('<int:tpk>/', views.NiceCommentListView.as_view(), name='comment_list'),
    path('<int:tpk>/<str:cpk>', views.NiceCommentListView.as_view(), name='comment_list'),
]