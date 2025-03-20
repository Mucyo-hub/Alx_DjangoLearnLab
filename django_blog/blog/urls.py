from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),  # List view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Detail view
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # Create view
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_edit'),  # Update view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Delete view
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/<int:pk>/edit_comment/', views.edit_comment, name='edit_comment'),
    path('posts/<int:pk>/delete_comment/', views.delete_comment, name='delete_comment'),
]
