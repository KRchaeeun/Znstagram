from django.db import models
from django.conf import settings

# Create your models here.

class Tag(models.Model):
    # content = models.TextField(unique=True)
    content = models.CharField(max_length=100, unique=True)  # 태그는 일반적으로 짧으므로 TextField 대신 CharField 사용

class Article(models.Model):
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255, blank=True)  # 사용자가 포스팅한 위치를 설정할 수 있는 위치 필드 추가
    image = models.ImageField(blank=True, upload_to = 'images/')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)