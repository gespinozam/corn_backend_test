# Generated by Django 3.2 on 2021-04-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lunch",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
