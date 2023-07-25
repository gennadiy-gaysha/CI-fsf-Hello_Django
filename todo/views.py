from django.shortcuts import render, redirect, get_object_or_404
# The next thing we need is the way to display those items to our users.
# So we need to find a way to get those items from the database into a
# template.
# Remember that in the Model View Template (MTV) design pattern
# The views represent the programming logic that allows users to interact with
# the database through the templates that they see.
# That means that we should probably start in views dot.py
# We need access to the item model in this file so the first thing I'm going
# to do is right at the top. From .models import item.
from .models import Item
from .forms import ItemForm


# Create your views here.

# We need to display items to our users
def get_todo_list(request):
    # Create a query set of all the items in the database.
    items = Item.objects.all()

    # Convert queryset to a dictionary
    # items_dict = items.values('name', 'done')
    #
    # context = {
    #     "items": items_dict,
    # }
    context = {
        "items": items,
    }
    # Adding context as a third argument to the render function ensures that
    # we have access to it in our todo_list.html template
    return render(request, "todo/todo_list.html", context)
    # Once we save this we've got everything we need to ensure complete
    # communication between the users of our app on the front end. And our
    # database on the back end.


def add_item(request):
    if request.method == "POST":
        # Now our new form from forms.py will create the Item instance:
        # But instead here will populate the form in Django with the
        # request.post data.
        form = ItemForm(request.POST)
        # ===================================================
        # First in the request.POST handler we create the Item manually:
        # name = request.POST.get("item_name")
        # checks if the "Done" checkbox was checked:
        # done = "done" in request.POST
        # Create a new Item object in the DB using the retrieved data:
        # Item.objects.create(name=name, done=done)
        # "get_todo_list" below is a view!!!
        # ===================================================
        # Then we can simply call the is_valid method on the form,
        # and Django will automatically compare the data submitted in the
        # post request to the data required on the model.
        if form.is_valid():
            # To save our item then all we need to do is call form.save and
            # then redirect to the get_todo list view like we were before.
            form.save()
        return redirect("get_todo_list")

    # With the form imported, we create the instance (prepared to fill in) of
    # it:
    form = ItemForm()
    # context contains the empty form:
    # The context variable is created as a Python dictionary containing
    # the form instance.
    context = {
        "form": form
    }
    # we return the context to the template:
    # The form instance is passed to the template as part of the context
    # dictionary:
    return render(request, "todo/add_item.html", context)

def edit_item(request, item_id):
    # In this view function, the parameter item_id receives the value from
    # the URL. The view uses item_id to retrieve the specific Item object
    # from the database using Django's get_object_or_404() function.
    # The get_object_or_404() function takes two arguments:
    # The model class to query (Item in this case).
    # The condition to filter the object(s) (in this case, filtering by the
    # id field to match item_id).
    # So, item = get_object_or_404(Item, id=item_id) searches the Item model
    # for an object with the id field matching the item_id received from the
    # URL. If an Item object with the specified id exists, it is returned and
    # assigned to the item variable. If no matching object is found, a 404
    # Not Found page is displayed.
    # ==========================================
    # It`s a copy of an Item from our database
    item = get_object_or_404(Item, id=item_id)
    # This is a POST handler:
    # ==========================================
    if request.method == "POST":
        # After retrieving the Item object, the view creates a form instance
        # (form) of the ItemForm class, which is a Django form representing
        # the Item model. The form is initialized with the data from the
        # user's POST request (request.POST) and the retrieved Item object
        # (instance=item).
        form = ItemForm(request.POST, instance=item)
        # The view then checks if the form is valid (form.is_valid()). This
        # validation involves checking if the data entered by the user in the
        # form fields is valid and matches the form's validation rules.
        # If the form is valid, the view saves the form, which updates the
        # corresponding Item object in the database with the edited data
        # provided by the user.
        if form.is_valid():
            form.save()
        return redirect("get_todo_list")
    # ==========================================
    # This is a GET handler:
    # ==========================================
    # To pre-populate the form with the items current details, we can pass an
    # instance argument to the form, telling it that it should be prefilled
    # with the information for the item we just got from the database.
    form = ItemForm(instance=item)
    context = {
        "form": form
    }
    return render(request, "todo/edit_item.html", context)

def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect("get_todo_list")

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect("get_todo_list")
