# Generated by Django 4.2 on 2023-04-17 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipeingredient_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item', models.CharField(max_length=150)),
                ('amount', models.CharField(max_length=150)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe')),
            ],
            options={
                'ordering': ['food_item'],
            },
        ),
        migrations.DeleteModel(
            name='RecipeIngredient',
        ),
    ]
