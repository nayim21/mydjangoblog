from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import HttpResponse


#def home(request):
#    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request,user)
            return HttpResponse('Hello Dear')

    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm (data=request.POST)
        if form.is_valid():
            user = form.get_user()
            return  HttpResponse('HELLO  DEAR')
            #return HttpResponse('Hello USER')
    else :
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
