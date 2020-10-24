from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status, viewsets
from django.shortcuts import render, get_object_or_404
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
        'create': [IsAuthenticated],
        'retrieve': [AllowAny],
        'update': [IsAuthenticated],

    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(ViewPostSerializer, self).get_serializer_class()

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


@api_view(['GET', ])
def blog_like_view(request, pk):
    if request.user.id == None:
        return Response({"detail": "Authentication credentials were not provided."})
    post = Post.objects.get(id=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', ])
# @permission_classes([IsAuthenticated])
def comment_list_view(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comments.all()
    serializer = ViewCommentSerializer(comments, many=True)
    return Response(serializer.data)


class CreateCommentView(CreateAPIView):
    serializer_class = CreateCommentSerializer
    permission_classes = [IsAuthenticated]
