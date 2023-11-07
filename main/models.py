from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    text = models.TextField()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)




