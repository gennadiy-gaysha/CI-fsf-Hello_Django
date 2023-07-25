"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path function typically takes 3 arguments: url that triggers
    # get_todo_list function, and name parameter
    path("", views.get_todo_list, name="get_todo_list"),
    path("add_item", views.add_item, name="add_item"),
    # <item_id> is a parameter that we include into edit_item parameter
    # In this URL pattern, the part <item_id> is a placeholder enclosed
    # in angle brackets, indicating that it will capture the value that
    # comes after "edit/" in the URL. For example, if a user visits the
    # URL "edit/42", the item_id parameter in the view function will be
    # assigned the value "42".
    path("edit/<item_id>", views.edit_item, name="edit"),
    path("toggle/<item_id>", views.toggle_item, name="toggle"),
    path("delete/<item_id>", views.delete_item, name="delete")
]
