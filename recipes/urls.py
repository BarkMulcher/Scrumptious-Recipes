"""scrumptious URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recipes.views import recipe_list, show_recipes, create_recipe, edit_recipe, user_recipes

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('<int:id>/', show_recipes, name='show_recipes'),
    path('create/', create_recipe, name='create_recipe'),
    path('<int:id>/edit', edit_recipe, name='edit_recipe'),
    path('mine/', user_recipes, name='user_recipes')
]


