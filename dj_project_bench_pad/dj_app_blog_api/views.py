from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend

from dj_app_blog.models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['body', 'author__profile__bio']
    ordering_fields = ['author_id', 'publish']
    ordering = ['body']

    # def get_queryset(self):
    #     user = self.request.user
    #     return Post.objects.filter(author=user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserPostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.kwargs['username']
        return Post.objects.filter(author=user)
