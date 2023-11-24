from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Genre3(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    genre_types = models.ForeignKey(Genre3, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    image_cover = models.ImageField(upload_to='covers', blank=True)
    file = models.FileField(upload_to='files', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('detail', )


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)




