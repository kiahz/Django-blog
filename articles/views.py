from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
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

@login_required(login_url='/accounts/login/')
def create_article(request):
    if request.method == 'POST':
        form = forms.create_article (request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('articles:List')
    else:
        form=forms.create_article()
    return render (request,'articles/create_article.html',{'form':form})