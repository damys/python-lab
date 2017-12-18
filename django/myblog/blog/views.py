from django.shortcuts import render

from django.http import HttpResponse
from . import models


def index(request):
    # return HttpResponse("hello Django")

    # return render(request, 'index/index.html' )

    article = models.Article.objects.get(pk=1)

    return render(request, 'index/index.html', {'article':article})