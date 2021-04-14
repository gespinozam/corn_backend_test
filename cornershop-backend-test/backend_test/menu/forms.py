from django import forms
from datetime import datetime, date

# Models to get model from DB
from .models import Lunch, Orders

"""
Forms to set 'form_class' in views for each View Class in views.py

# CreateMenuForm to CreateLunch class
# UpdateMenuForm to UpdateLunch class
# DeleteMenuForm to DeleteLunch class
# OrderMenuForm to OrderLunch class
"""


class CreateMenuForm(forms.ModelForm):
    class Meta:
        model = Lunch
        fields = ("name", "details", "add_time", "is_active")


class UpdateMenuForm(forms.ModelForm):
    class Meta:
        model = Lunch
        fields = ("name", "details", "is_active")


class DeleteMenuForm(forms.ModelForm):
    class Meta:
        model = Lunch
        fields = "__all__"


class OrderMenuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderMenuForm, self).__init__(*args, **kwargs)
        self.fields["lunch"].queryset = Lunch.objects.filter(add_time=date.today())

    class Meta:
        model = Orders
        fields = ("lunch", "custom")
