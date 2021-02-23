from django.shortcuts import render
from django.shortcuts import HttpResponse , redirect
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
# Create your views here.
def article_list(request):
    artcvalue=models.Article.objects.all().order_by('date')
    return render(request,'articlelist.html',{'xartc':artcvalue})
def article_detail (request , valslug) :
#    return HttpResponse (valslug)
    valarticle=models.Article.objects.get(slug=valslug)
    return render(request,'articledetail.html',{'valarticle2':valarticle})

@login_required (login_url = "/accounts/login")
def article_create (request):
    if request.method == 'POST' :
        form=forms.CreateArticle(request.POST)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect ('articles:list')
    else :
        form = forms.CreateArticle()
        return render(request,'create.html',{'form': form })
