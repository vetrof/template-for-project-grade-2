from rest_framework import serializers

from main.models import Article, Like, Genre3


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'article']


class Genre3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Genre3
        fields = ['id', 'name',]


class ArticleSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    genre_types = Genre3Serializer()

    class Meta:
        model = Article
        fields = ['id', 'title', 'image_cover', 'text',  'genre_types', 'like_count', 'file']

    @staticmethod
    def get_like_count(obj):
        return obj.like_set.all().count()



