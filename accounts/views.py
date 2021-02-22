from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout
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
            return HttpResponse('Hello Dear to sign up page')

    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm (data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login (request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else :
                return  HttpResponse('HELLO  DEAR to login page')
            #return HttpResponse('Hello USER')
    else :
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
def logout_view (request) :
    if request.method == 'POST' :
        logout(request)
        return HttpResponse('LOGOUT Dear')
