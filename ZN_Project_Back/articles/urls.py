from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='article_list'),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_ud),
]