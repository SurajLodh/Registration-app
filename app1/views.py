from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, response
from django.shortcuts import render
from .forms import ResgisterForm

# Create your views here.

def Home(response):

    return render(response, 'home.html')

def Register(response):
    if response.method == "POST":
        form = ResgisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        return redirect('/register')
    else:
        form = ResgisterForm()

    return render(response, 'register.html', {'form':form})


def Profile(response):
    

    return render(response, 'profile.html')