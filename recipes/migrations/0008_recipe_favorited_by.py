# Generated by Django 3.0.6 on 2020-06-19 19:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0007_recipe_public"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="favorited_by",
            field=models.ManyToManyField(
                related_name="favorite_recipes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
