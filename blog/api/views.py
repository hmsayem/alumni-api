from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status, viewsets
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from blog.models import Post
from blog.api.serializers import (
    ViewPostSerializer,
    CreatePostSerializer,
    UpdatePostSerializer,
    ViewCommentSerializer,
    CreateCommentSerializer,

)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ViewPostSerializer

    action_serializers = {
        'create': CreatePostSerializer,
        'update': UpdatePostSerializer
    }
    permission_classes = [IsAuthenticated]
    permission_classes_by_action = {
        'list': [AllowAny],
        'create': [AllowAny],
        'retrieve': [AllowAny],
        'update': [AllowAny],
        'destroy': [AllowAny],
    }

    def update(self, request, *args, **kwargs):
        blog = self.get_object()
        if blog.author.id != request.user.id:
            return Response({"detail": "Not allowed"})
        serializer = self.get_serializer(blog, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        blog = self.get_object()
        if blog.author.id != request.user.id:
            return Response({"detail": "Not allowed"})
        self.perform_destroy(blog)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)
        return super(ViewPostSerializer, self).get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


@api_view(['PUT', ])
def blog_like_view(request, pk):
    if request.user.id is None:
        return Response({"detail": "Authentication credentials were not provided."})
    post = Post.objects.get(id=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', ])
def comment_list_view(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comments.all()
    serializer = ViewCommentSerializer(comments, many=True)
    return Response(serializer.data)


class CreateCommentView(CreateAPIView):
    serializer_class = CreateCommentSerializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
