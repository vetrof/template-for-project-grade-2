from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from main.forms import ArticleForm
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

    if request.POST:
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            prev_url = request.session.get('prev_url_edit')
            if prev_url:
                return redirect(prev_url)
            else:
                return redirect('index')

    form = ArticleForm(instance=article)
    request.session['prev_url_edit'] = request.META.get('HTTP_REFERER')

    context = {'user_id': user_id,
               'article_id': article_id,
               'like_count': like_count,
               'button_label': button_label,
               'form': form,
               'article': article
               }

    return render(request, 'index.html', context)


def like(request):
    previous_page = request.META.get('HTTP_REFERER')

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

    # Проверка заголовка X-Requested-With для определения AJAX-запроса
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'button_label': button_label, 'like_count': like_count})

    if previous_page and previous_page != request.path_info:
        return redirect(previous_page)
    return redirect('index_page')


