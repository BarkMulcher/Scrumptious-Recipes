from django.contrib import admin
from recipes.models import Recipe, RecipeStep, Ingredient

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id',
        'description',
        'calories',
    ]

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = [
        'step_number',
        'instruction',
        'id'
    ]

@admin.register(Ingredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = [
        'food_item',
        'amount',
        'id'
    ]

