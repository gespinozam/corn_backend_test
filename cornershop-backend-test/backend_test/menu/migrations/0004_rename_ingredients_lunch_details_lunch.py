# Generated by Django 3.2 on 2021-04-12 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0003_auto_20210412_2127"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lunch",
            old_name="ingredients",
            new_name="details_lunch",
        ),
    ]