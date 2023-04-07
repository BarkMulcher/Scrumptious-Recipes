from django.forms import ModelForm
from recipes.models import Recipe
from django.views.generic.edit import UpdateView

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
                'title',
                'pic',
                'description'
            ]
        