from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
# Create your views here.
def article_list(request):
    artcvalue=models.Article.objects.all().order_by('date')
    return render(request,'articlelist.html',{'xartc':artcvalue})
def article_detail (request , valslug) :
#    return HttpResponse (valslug)
    valarticle=models.Article.objects.get(slug=valslug)
    return render(request,'articledetail.html',{'valarticle2':valarticle})
