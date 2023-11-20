from django.contrib import admin

from main.models import Article, Like

from django_summernote.admin import SummernoteModelAdmin


class ArticleAdmin(SummernoteModelAdmin):
    search_fields = ['text']
    summernote_fields = '__all__'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Like)
