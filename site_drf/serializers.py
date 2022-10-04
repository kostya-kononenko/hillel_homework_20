from rest_framework import serializers
from site_drf.models import Post, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'posts', 'comments']


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'text_comment', 'author', 'post']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'full_description', 'author', 'comments']