# Generated by Django 4.1.7 on 2023-05-09 10:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="following",
            field=models.ManyToManyField(
                related_name="followed_books", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
