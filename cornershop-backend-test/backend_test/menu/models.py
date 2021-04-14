from uuid import uuid4
from datetime import date
from django.db import models

# Import authentication django model
from django.contrib.auth.models import User

"""
Set Models to makemigrations and migrate

Lunch and Orders models to set menu data in DB

*Lunch*

:param id: ID of the Lunch to query for.
:param name: Name of the menu to save.
:param add_time: Field that saves the day of the menu to show, by default is today.
:param update_time: Last updated menu field, by default is now.
:param is_active: Flag to activate or deactivate a menu, by default is True.
:param details: Description of the menu or chef's observations.

:type id: UUID
:type name: Char
:type add_time: Date
:type update_time: DateTime
:type is_active: Bool
:type details: Char


*Orders*

:param lunch: ID of lunch of the Order to query for. Is a foreign key.
:param user: ID of the user registered with the order. Is a foreign key.
:param order_date: Field that saves the date when the menu was requested, by default is today.
:param custom: Customization of the user ordered menu.

:type lunch: UUID
:type user: Int
:type order_date: Date
:type custom: Char
"""


class Lunch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    add_time = models.DateField(default=date.today)
    update_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    details = models.CharField(default="", max_length=200)

    def __str__(self):
        return self.name

    def is_active_field(self):
        return self.is_active == True


class Orders(models.Model):
    lunch = models.ForeignKey(Lunch, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    order_date = models.DateField(auto_now_add=True)
    custom = models.CharField(default="", max_length=200)

    def __str__(self):
        return f"{self.order_date}"


"""
----------------------------------------------------------------------
"""

"""
Process to initialize data in db
"""
import json
import os
from django.contrib.auth.hashers import make_password

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DIR = BASE_DIR + "/menu/static/"


"""
Use first "python manage.py migrate" command to create DB.
Then uncomment this code to create database on the next "dev up" command

Initial page: http://0.0.0.0:8000/login/
"""


# def initial_models():
#     if User.objects.all().count() == 0:
#         with open(FILE_DIR + "initial_user_data.json", "r") as f:
#             user_obj = json.load(f)
#         with open(FILE_DIR + "initial_dummy_data.json", "r") as f:
#             dummy_obj = json.load(f)

#         for item in user_obj:
#             save_users = User()
#             save_users.username = item["username"]
#             save_users.password = make_password(item["password"])
#             save_users.is_superuser = item["is_superuser"]
#             save_users.save()

#         for item in dummy_obj:
#             save_menu = Lunch()
#             save_menu.name = item["name"]
#             save_menu.details = item["details"]
#             save_menu.is_active = item["is_active"]
#             save_menu.add_time = item["add_time"]
#             save_menu.save()

#         return print("READY")


# initial_models()

"""
----------------------------------------------------------------------
"""