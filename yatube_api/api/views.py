from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter

from api.permission import OwnerOrReadOnly
from posts.models import Post, Group

import api.serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = api.serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, OwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = api.serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, OwnerOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)


class ListOrRetriewe(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    pass


class GroupViewSet(ListOrRetriewe):
    queryset = Group.objects.all()
    serializer_class = api.serializers.GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ListOrCreate(mixins.ListModelMixin, mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    pass


class FollowViewSet(ListOrCreate):
    serializer_class = api.serializers.FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter,)
    search_fields = ('=following__username', '=user_username')

    def get_queryset(self):
        return self.request.user.following

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
