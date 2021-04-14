# Generated by Django 3.2 on 2021-04-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0002_alter_lunch_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="lunch",
            name="ingredients",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="lunch",
            name="update_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
