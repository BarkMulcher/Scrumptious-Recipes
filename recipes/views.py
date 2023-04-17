from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from recipes.forms import RecipeForm, SignUpForm
from recipes.models import Recipe
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.conf import settings

def show_404(request, exception):
    return render(request, '404/404.html')



def user_signup(request):
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['username']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']

            return redirect("main_page")
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

# @login_required
def show_recipes(request, id):
    # return HttpResponse('this view is working')
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        "recipe_object": recipe,
    }

    return render(request, 'recipes/detail.html', context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        'recipe_list': recipes,
    }
    return render(request, 'recipes/index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        # validate form inputs and save:
        if form.is_valid():
            form.save()
            # if is_valid=True, redirect
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    context = {
        'recipe_form': form
    }
    return render(request, 'recipes/create.html', context)


def edit_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        # validate the inputs
        if form.is_valid():
        #  save to database:
            form.save()
        # If all goes well, we can redirect the browser
        #   to another page
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    context = {
        'form': form
    }
    return render(request, 'recipes/edit.html', context)

