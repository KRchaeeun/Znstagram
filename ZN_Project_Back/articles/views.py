from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404, render

from .serializers import ArticleListSerializer, ArticleSerializer, ArticleSerializer, CommentSerialzer
from .models import Article, Comment
from accounts.models import User


# 게시물 조회 및 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def articles_list(request):
    if request.method == 'GET':
        article = Article.objects.all()
        serializer = ArticleListSerializer(article, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시물 상세 조회 및 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, article_pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'message': '게시물이 삭제되었습니다.'
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)



# 댓글 조회 및 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, article_pk=article_pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(article_pk=article.pk).order_by('-created_at')
        serializer = CommentSerialzer(comments, many=True)
        return Response(serializer.data)
      
    if request.method == 'POST':
        serializer = CommentSerialzer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 수정 및 삭제
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_ud(request, comment_pk):
    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({'message': '권한이 없습니다.'})

    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'DELETE':
        comment.delete()
        data = {
            'message': '댓글이 삭제되었습니다.'
        }
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerialzer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)