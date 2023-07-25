from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # In the test method, we create an instance of the ItemForm by
        # passing a dictionary with an empty value for the name field:
        form = ItemForm({"name": ""})
        self.assertFalse(form.is_valid())
        # This line asserts that the key "name" exists in the form.errors
        # dictionary. If the "name" field has an error, it will be listed
        # in the form errors dictionary.
        self.assertIn("name", form.errors.keys())
        # self.assertEqual(form.errors["name"][0], "This field is required")
        # checks if the first error message associated with the "name" field
        # in the form.errors dictionary is "This field is required". This
        # ensures that the correct error message is being displayed when the
        # "name" field is left empty.
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_done_field_is_not_required(self):
        form = ItemForm({"name": "Test Todo Item"})
        self.assertTrue(form.is_valid())


    # The only fields that displayed in the form are "name" and "done" fields
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
