from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404, render

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerialzer
from .models import Article, Comment
from accounts.models import User