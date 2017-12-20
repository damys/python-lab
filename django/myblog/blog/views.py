from django.shortcuts import render

from django.http import HttpResponse
from . import models


def index(request):
    # return HttpResponse("hello Django")

    # return render(request, 'blog/blog.html' )

    # 获取一条
    # article = models.Article.objects.get(pk=1)
    # return render(request, 'blog/index.html', {'article': article})

    # 获取所有
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles':articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article':article})


def edit_page(request, article_id):

    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article':article })




def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        """ 添加 """
        models.Article.objects.create(title=title, content=content)
        # 返回首页，显示全部
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles':articles})

    """ 修改 """
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})