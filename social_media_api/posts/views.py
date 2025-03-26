from rest_framework import viewsets, permissions,generics,status
from .models import Post, Comment,Like
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, CommentSerializer,LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend

CustomUser = get_user_model()  # Get the custom user model


class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            return Response({"message": "Post liked successfully"}, status=status.HTTP_201_CREATED)
        return Response({"message": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({"message": "Post unliked successfully"}, status=status.HTTP_200_OK)
        return Response({"message": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)

class UserFeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users access the feed

    def get(self, request):
        # Get the list of users the authenticated user follows
        following_users = request.user.following.all()
        
        # Filter posts from followed users and order by creation date (latest first)
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

