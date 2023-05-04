# Generated by Django 4.1.7 on 2023-05-04 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Loan", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="loan",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="loaned_for",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
