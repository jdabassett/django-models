# Generated by Django 5.0 on 2023-12-14 05:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("snacks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="snack",
            name="date_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]