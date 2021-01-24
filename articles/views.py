from django.shortcuts import render
from . import models
# Create your views here.
def article_list(request):
    artcvalue=models.Article.objects.all().order_by('date')
    return render(request,'articlelist.html',{'xartc':artcvalue})
