from rest_framework import serializers

from main.models import Article, Like


# TODO сделать вывод лайков по пользователю
# TODO сделать добавление лайка
# TODO сделать редактирование статьи


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'article']


class ArticleSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'image_cover', 'text', 'like_count']

    def get_like_count(self, article):
        return Like.objects.filter(article=article).count()

