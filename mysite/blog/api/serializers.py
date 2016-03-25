from django.contrib.auth.models import User, Group
from blog.models import Post, Article
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ('title', 'slug', 'text', 'created_date', 'tags')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Article
        fields = ('title', 'slug', 'content', 'created_date', 'tags')


