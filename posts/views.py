from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from thebod_drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    '''
    Handles listing and creating posts in the API.
    Includes:
    - Annotated like/comment counts.
    - Filtering by owner, tags, likes, and followed profiles.
    - Search by title, tags, and owner's username.
    - Ordering by comments, likes, or like creation date.
    '''
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_total=Count('likes', distinct=True),
        comments_total=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__profile',
        'tags',
        'likes__owner__profile',
        'owner__followed__owner__profile',
    ]
    search_fields = [
        'title',
        'tags',
        'owner__username'
    ]
    ordering_fields = [
        'comments_total',
        'likes_total',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        '''
        Customizes the creation process by assigning the currently authenticated user
        as the owner of the object being created.
        '''
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_total=Count('likes', distinct=True),
        comments_total=Count('comment', distinct=True)
    ).order_by('-created_at')