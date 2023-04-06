from pydoc import describe
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    pic = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    calories = models.SmallIntegerField(null=True, blank=True)
    made_this = models.BooleanField(default=False)
