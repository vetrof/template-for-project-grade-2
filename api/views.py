from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import ArticleSerializer
from main.models import Article
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
class ArticleListViewSet(ModelViewSet):
    # http_method_names = ['get']
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    # permission_classes = [IsAuthenticated]


