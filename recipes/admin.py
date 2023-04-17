from django.contrib import admin
from recipes.models import Recipe, RecipeSteps

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id',
        'description',
        'calories',
    ]

@admin.register(RecipeSteps)
class RecipeStepsAdmin(admin.ModelAdmin):
    list_display = [
        'recipe_title',
        'order',
        'id'
    ]