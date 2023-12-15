from django.db import models
from django.conf import settings


# 해시태그 모델
class Tag(models.Model):
    # content = models.TextField(unique=True)
    content = models.CharField(max_length=100, unique=True)  # 태그는 일반적으로 짧으므로 TextField 대신 CharField 사용

    def get_articles(self):
        return self.article_set.all()  # 특정 태그가 있는 게시물 반환. 태그 검색 기능 구현 가능


# 게시글 모델
class Article(models.Model):
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255, blank=True)  # 사용자가 포스팅한 위치를 설정할 수 있는 위치 필드 추가
    image = models.ImageField(blank=True, upload_to = 'images/')
    # 이미지 파일 크기를 최적화 코드가 필요
    # 이미지를 자동으로 압축하고 크기를 조정하는 방법은 
    # 1. Pillow 라이브러리 사용
    # 2. Custom ImageField
    # 3. 저장 시점에서 이미지 처리
    # 4. django-imagekit과 같은 서드 파티 라이브러리 사용

    def like_count(self):
        return self.articlelike_set.count()  # 해당 게시물에 대한 좋아요 수 계산
    

# 댓글 모델
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)  # 어떤 댓글이 다른 댓글에 대한 답변인지를 구조적으로 나타내는 스레드 댓글을 위한 자기 참조 외래키
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def like_count(self):
        return self.commentlike_set.count()  # 해당 댓글에 대한 좋아요 수 계산


class ArticleLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'article')  # 동일 사용자가 동일 게시물에 중복 좋아요 방지


class CommentLike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        unique_together = ('user', 'comment')  # 동일 사용자가 동일 댓글에 중복 좋아요 방지


class Report(models.Model):
    REPORT_CHOICES = [
        ('spam', 'Spam'),
        ('abuse', 'Abuse'),
        ('other', 'Other'),
    ]

    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')  # 신고를 한 사용자
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='article_reports')  # 신고된 게시물
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='comment_reports')  # 신고된 댓글
    reason = models.CharField(max_length=50, choices=REPORT_CHOICES)  # 신고 이유 필드. 리스트로 제공
    details = models.TextField(blank=True)  # 신고에 대한 추가적인 상세 설명
    created_at = models.DateTimeField(auto_now_add=True)  # 신고가 생성된 시간
    is_resolved = models.BooleanField(default=False)  # 신고가 처리되었는지 여부

    def __str__(self):
        return f"Report by {self.reported_by} on {self.article or self.comment}"