from django.forms import ModelForm, Form
from recipes.models import Recipe
from django.views.generic.edit import UpdateView
from pydoc import describe
from django.db import models
from django.conf import settings
from django import forms

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
                'title',
                'pic',
                'description'
            ]

