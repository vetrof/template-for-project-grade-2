from django.contrib import admin

from main.models import Article, Like, Genre3

from django_summernote.admin import SummernoteModelAdmin


class ArticleAdmin(SummernoteModelAdmin):
    search_fields = ['text']
    summernote_fields = '__all__'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Genre3)
admin.site.register(Like)
