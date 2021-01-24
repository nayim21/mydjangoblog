from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse
def about(request):
    return HttpResponse('Hello World')
def home(request):
    return HttpResponse('Home')
