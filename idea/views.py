from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import nameForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form=UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                messages.error(request, form.errors)
        context ={'form' : form}
        return render(request, 'users/register.html',context)

def loginPage(request):
     if request.user.is_authenticated:
        return redirect('home')
     else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user= authenticate(request , username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('error')
        context={}
        return render(request, 'users/login.html',context)
def logoutuser(request):
    logout(request)
    return redirect('home')


def username(request):
    form=nameForm()
    if request.user.is_authenticated:
        form = nameForm(request.POST , instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('login')
        context = {'form' : form}
        return render(request, 'users/username.html',context)
    else:
        return redirect('home')

def house(request):
    return render(request, 'users/home.html')
def error(request):
    return render(request, 'users/error_message.html')