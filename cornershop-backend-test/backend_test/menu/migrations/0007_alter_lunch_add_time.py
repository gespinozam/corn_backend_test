# Generated by Django 3.2 on 2021-04-12 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0006_alter_lunch_details"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lunch",
            name="add_time",
            field=models.DateField(auto_now_add=True),
        ),
    ]