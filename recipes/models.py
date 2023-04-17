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
        USER_MODEL,
        related_name='recipes',
        on_delete=models.CASCADE,
        null=True
                )

    def __str__(self):
        return self.title

class RecipeSteps(models.Model):
    instruction = models.CharField(max_length=500)
    order = models.PositiveIntegerField()
    recipe = models.ForeignKey(
        Recipe,
        related_name='steps',
        on_delete=models.CASCADE
    )

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        # referring to order column(?) from above
        ordering = ['order']
        # must run makemigrations and migrate after any changes
        # to see migs, run 'showmigrations'

