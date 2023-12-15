from rest_framework import serializers
from .models import Article, Comment, Tag, ArticleLike

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'content')


class CommentSerialzer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        depth = 1
        fields = '__all__'
        read_only_fields = ('user',)


class ArticleSerializer(serializers.ModelSerializer):

    comment_set = CommentSerialzer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'tag')