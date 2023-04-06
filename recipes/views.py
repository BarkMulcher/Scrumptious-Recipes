from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from recipes.models import Recipe
from django.conf import settings
from django.shortcuts import redirect


# always takes 'request' as parameter
def show_main(request):
    return render(request, 'main/index.html')

def show_create(request):
    return render()

def show_404(request, exception):
    return render(request, '404/404.html')

def show_recipes(request, id):
    # return HttpResponse('this view is working')
    recipe = get_object_or_404(Recipe, id=id)
    print(recipe)
    context = {
        "recipe_object": recipe,
    }

    return render(request, 'recipes/detail.html', context)
