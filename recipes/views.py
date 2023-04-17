from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from recipes.forms import RecipeForm
from recipes.models import Recipe
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django import forms
from django.conf import settings

# user = User.objects.create_user('Luke', 'luke@gmail.com', 'lukepassword')

def show_404(request, exception):
    return render(request, '404/404.html')



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

@login_required()
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        # validate form inputs and save:
        if form.is_valid():
            recipe = form.save(False)
            # if is_valid=True, redirect
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    context = {
        'form': form
    }
    return render(request, 'recipes/create.html', context)

@login_required
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

@login_required()
def user_recipes(request):
    recipes = Recipe.objects.filter(author=request.user)
    context = {
        'recipe_list': recipes,
    }
    return render(request, 'recipes/index.html', context)