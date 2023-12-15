from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='article_list'),  # 전체 게시글 목록
    path('<int:article_pk>/', views.article_detail, name='article_detail'),  # 특정 게시글 상세 보기
    path('<int:article_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_ud),
]