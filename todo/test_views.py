from django.test import TestCase
from .models import Item

# In the context of a class, self refers to the instance of that class.
# When defining methods in a class, including test methods in a Django
# TestCase subclass, the first parameter is conventionally named self.
# This parameter represents the instance of the class that the method is
# being called on.

# In the Django TestCase class and other Python classes, self allows you to
# access and modify the attributes and methods of the current instance. It
# is a reference to the instance itself, enabling you to work with instance-
# specific data and behavior.

# Create your tests here.
# We want to test not only that our views return a successful HTTP response
# and that they're using the proper templates, but also what they can do,
# specifically adding toggling and deleting items.


class TestViews(TestCase):
    # the test client sends a GET request to the root URL (/).
    # The self.client is a built-in test client provided by Django,
    # and get() is a method that simulates making a GET request to
    # the specified URL.
    def test_get_todo_list(self):
        # The self.client object is an instance of the django.test.Client
        # class, which is a special-purpose test client that allows you to
        # simulate HTTP requests and responses without actually running a
        # server.

        # When the test client sends the GET request to the root URL,
        # Django's URL dispatcher matches the URL to the corresponding URL
        # pattern in the urls.py. In this case, it finds the URL pattern that
        # maps the root URL ('/') to the get_todo_list view function.
        # View Processing: The get_todo_list function is executed and
        # processes the request. In this case, the view returns an HTTP
        # response, possibly rendered using a template.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')
        # print(response.status_code)
        # print(response.headers)
        # print(response.content.decode("utf-8"))

    def test_get_add_item_page(self):
        response = self.client.get("/add_item")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        # In this line, a new Item object is created and saved to the database
        # with the name "Test Todo Item". This item will be used to simulate
        #  the edit page.
        item = Item.objects.create(name="Test Todo Item")
        # This line simulates a GET request to the URL path edit/<item.id>,
        # where <item.id> is the ID of the newly created Item object.
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/edit_item.html")
        # print(response.status_code)
        # print(response.headers)
        # print(response.content.decode("utf-8"))

    def test_can_add_item(self):
        # response = self.client.post(...): The self.client.post() method
        # sends the POST request to the view associated with "/add_item" and
        # captures the response returned by the view. The response object
        # contains information about the server's response to the request.
        response = self.client.post('/add_item', {"name": "Test Added Item"})
        # self.assertRedirects(response, "/"): This line verifies whether the
        # server's response redirects to the root URL ("/") after adding the
        # new item. The self.assertRedirects() method checks if the response
        # status code is a redirect status code (e.g., 301 or 302) and if the
        # response "Location" header matches the expected redirect URL ("/").
        self.assertRedirects(response, "/")
        print(response.status_code) # 302
    # ========================================================================

    # ========================================================================
    def test_can_toggle_item(self):
        # Create Test Item: The test starts by creating a new Item object in
        # the database with the name "Test Added Item" and done=True using
        # the Item.objects.create() method. This item is created to have the
        # done field initially set to True.
        item = Item.objects.create(name="Test Added Item", done=True)
        # We simulate a GET request to the URL path '/toggle/<item.id>',
        # where <item.id> is the ID of the test item created in the previous
        # step. The test client's self.client.get() method is used to simulate
        # the request.
        response = self.client.get(f"/toggle/{item.id}")
        self.assertRedirects(response, "/")
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)


    def test_can_delete_item(self):
        item = Item.objects.create(name="Test Added Item")
        # We simulate a DELETE request to the URL path '/delete/<item.id>',
        # where <item.id> is the ID of the item created in the previous step.
        # The test client's self.client.get() method is used to simulate the
        # request.
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/') # gives us status_code 302
        print(response.status_code)  # 302
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)
