from django.test import TestCase
from .models import Item

# We test that our todo items will be created by default with the done
# status of false.
class TestModels(TestCase):
    def test_done_defaults_to_false(self):
        item = Item.objects.create(name="Test Todo Item")
        self.assertFalse(item.done)