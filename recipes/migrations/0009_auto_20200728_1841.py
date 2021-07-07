# Generated by Django 3.0.8 on 2020-07-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0008_recipe_favorited_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="photo",
            field=models.ImageField(
                blank=True,
                height_field="photo_height",
                null=True,
                upload_to="recipe_photos/",
                width_field="photo_width",
            ),
        ),
        migrations.AddField(
            model_name="recipe",
            name="photo_height",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="photo_width",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
