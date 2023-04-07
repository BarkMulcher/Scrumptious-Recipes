from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from recipes.forms import RecipeForm
from recipes.models import Recipe
from django.shortcuts import redirect

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

