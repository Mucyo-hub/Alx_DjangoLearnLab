from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentCreateView,CommentUpdateView,CommentDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),  # List view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Detail view
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # Create view
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),  # Update view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Delete view
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]
