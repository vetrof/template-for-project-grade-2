from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from api.serializers import ArticleSerializer
from main.models import Article
from rest_framework.permissions import IsAuthenticated


class ArticlePagination(PageNumberPagination):
    page_size = 2  # Количество объектов на странице
    page_size_query_param = 'page_size'
    max_page_size = 100


# @csrf_exempt
class ArticleListViewSet(ModelViewSet):
    # http_method_names = ['get']
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    pagination_class = ArticlePagination
    # permission_classes = [IsAuthenticated]


