from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def logout_user(request):
    logout(request)
    return redirect('accounts:login')

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    print(username)
    if user is not None:
        print('entrou 1')
        login(request, user)
        return redirect('accounts:home')
    else:
        print('entrou 2')
    return redirect('accounts:login')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('accounts:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def forgotP(request):
    return render(request, 'accounts/forgot_password.html')

def forgotE(request):
    return render(request, 'accounts/forgot_email.html')