from django.shortcuts import render
from django.http import HttpResponse #this is not needed when all the returns are render()

from django.http import Http404
from .models import article


def index(request):
    article_list = article.objects.order_by('-pub_date')[:5]
    context = {
        'article_list': article_list,
    }
    return render(request, 'article/index.html', context)


def short(request, code):
    return HttpResponse("You're looking at the short view of artilce %s." % code)


def abstract(request, code):
    return HttpResponse("You're looking at the abstract view of artilce %s." % code)


def full(request, code):
    try:
        a = article.objects.get(code=code)

    except article.DoesNotExist:
        raise Http404("Article does not exist")
    return render(request, 'article/full.html', {'article': a})


    # article_full = article.objects.order_by('-pub_date')[:5]
    # context = {
    #     'article_list': article_full,
    # }
    # return render(request, 'article/full.html', context)