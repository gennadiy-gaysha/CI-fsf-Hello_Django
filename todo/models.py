# Imports the model's folder from the Django / DB directory in our project ' \
#                 'site-packages.
# Imports the models module from Django, which contains classes and utilities
# for defining database models.
from django.db import models

# Create your models here.
# Item inherits from models.Model, which is the base class provided by Django \
# for database models.

# By defining the Item model with these fields, Django will automatically
# create a corresponding table in the database when migrations are applied.
# The table will have columns for name and done, matching their respective
# data types (text and boolean).

# In Item, we inherit the base Model class


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
# This will change how our items are displayed (in Admin panel etc.)
#     def __bool__(self):
#         return self.done
    def __str__(self):
        return self.name
