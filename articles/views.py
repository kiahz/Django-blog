from http.client import responses

from django.shortcuts import render,HttpResponse
from . import models
def articles_list(request):
    articles=models.Article.objects.all().order_by('-date')
    #tamame object haye article k save krdim ro migire
    args={'articles':articles}
    #va hamasho dakhel in save mikone va mide be return
    return render(request,'articles/articles_list.html',args)

def articles_detail(request,slug):
    # return HttpResponse(slug)
    article=models.Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})

