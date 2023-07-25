# In Django it's possible to create forms directly from the model itself.
# And allow Django to handle all the form validation.
# To make this happen we need to create a new file in the todo app directory
# called forms.py
from django import forms
from .models import Item

# Our form will be a class that inherits a built-in Django class to give it
# some basic functionality.

class ItemForm(forms.ModelForm):
    # We tell the form which model it will be associated with and then the
    # form can be rendered out as our template variable
    class Meta:
        model = Item
        fields = ["name", "done"]
