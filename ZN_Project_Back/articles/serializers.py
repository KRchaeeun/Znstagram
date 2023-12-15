from rest_framework import serializers
from .models import Article, Comment, Tag, ArticleLike, CommentLike, Report


# 해시태그 시리얼라이져
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# 전체 게시글 시리얼라이져
class ArticleListSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()  # 좋아요 수를 나타내는 필드 추가

    class Meta:
        model = Article
        fields = ('id', 'content', 'like_count')


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