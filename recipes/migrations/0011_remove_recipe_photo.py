# Generated by Django 3.1.1 on 2020-09-08 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0010_auto_20200728_1941"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="photo",
        ),
    ]
