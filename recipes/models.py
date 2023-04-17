from pydoc import describe
from django.db import models
from django.conf import settings

#  get the name of the class used for the user
USER_MODEL = settings.AUTH_USER_MODEL

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    pic = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    calories = models.SmallIntegerField(null=True, blank=True)
    made_this = models.BooleanField(default=False)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='recipes',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title

class RecipeStep(models.Model):
    step_number = models.SmallIntegerField(null=True)
    instruction = models.TextField()
    order = models.PositiveIntegerField()
    recipe = models.ForeignKey(
        Recipe,
        related_name='steps',
        on_delete=models.CASCADE,
    )

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        # referring to order column(?) from above
        ordering = ['order']
        # must run makemigrations and migrate after any changes
        # to see migs, run 'showmigrations'

class Ingredient(models.Model):
    food_item = models.CharField(max_length=150)
    amount = models.CharField(max_length=150)
    recipe = models.ForeignKey(
        Recipe,
        related_name='ingredients',
        on_delete=models.CASCADE)

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        ordering = ['food_item']

    print(food_item)

# class Author(models.Model):
#     author = models.CharField(max_length=150)
#     recipe = models.ForeignKey(
#         Recipe,
#         related_name='author',
#         on_delete=models.CASCADE)
