from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from main.models import Like, Article


def index(request):
    article_id = 1
    user_id = request.user.id
    article = Article.objects.get(id=article_id)
    like_count = article.like_set.count()
    user_has_liked = Like.objects.filter(user_id=user_id, article_id=article_id).exists()

    if user_has_liked:
        button_label = 'UnLike'
    else:
        button_label = 'Like'

    print(like_count)
    return render(request, 'index.html', {'user_id': user_id, 'article_id': article_id, 'like_count': like_count,
                                          'button_label': button_label})


@login_required
def like(request):
    article_id = request.POST.get('article_id')
    user_id = request.POST.get('user_id')

    if Like.objects.filter(user_id=user_id, article_id=article_id).exists():
        obj = Like.objects.filter(user_id=user_id, article_id=article_id)
        obj.delete()
        button_label = 'Like'
    else:
        like_obj = Like(user_id=user_id, article_id=article_id)
        like_obj.save()
        button_label = 'Unlike'

    like_count = Article.objects.get(id=article_id).like_set.count()
    return JsonResponse({'button_label': button_label, 'like_count': like_count})


