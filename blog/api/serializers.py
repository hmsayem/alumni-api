from rest_framework import serializers
from blog.models import Post, Comment, Category


class ViewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'date', 'author', 'title', 'header_image', 'category', 'body']
        extra_kwargs = {'author': {'required': False}}


class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'date', 'author', 'title', 'header_image', 'category', 'body']
        read_only_fields = ['author']


class ViewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'user', 'body', 'timestamp']
