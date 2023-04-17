from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from accounts.forms import SignUpForm, LoginForm
from django import forms
from recipes.views import show_404

def create_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['username']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            password_conf = form.cleaned_data['password']

            if password == password_conf:
                user = User.objects.create_user(
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    password = password,
                )
                user.save()

                return redirect("recipe_list")
            else:
                form.add_error('password', '''passwords don't match''')
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username,
            password=password)
            if user is not None:
                login(request, user)
                return redirect('recipe_list')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('recipe_list')