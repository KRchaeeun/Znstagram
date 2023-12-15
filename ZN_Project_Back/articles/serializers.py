from rest_framework import serializers
from .models import Article, Comment, Tag, ArticleLike, CommentLike, Report


# 해시태그 시리얼라이져
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# 게시글 좋아요 시리얼라이져
class ArticleLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLike
        fields = '__all__'


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'


# 전체 게시글 시리얼라이져
class ArticleListSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()  # 좋아요 수를 나타내는 필드 추가

    class Meta:
        model = Article
        fields = ('id', 'content', 'like_count')
    
    def get_like_count(self, obj):  # 게시글 모델의 인스턴스에 대해 좋아요 개수를 계산하여 반환
        return obj.like_count()  


# 댓글 시리얼라이져
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        depth = 1
        fields = '__all__'
        read_only_fields = ('user',)


# 단일 게시글 시리얼라이져
class ArticleSerializer(serializers.ModelSerializer):

    comment_set = CommentSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()  # 좋아요 수를 나타내는 필드 추가
    tags = TagSerializer(many=True, read_only=True)   # 태그 정보를 포함

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user')  # 위에 tags는 별도의 TagSerializer로 처리하므로 삭제