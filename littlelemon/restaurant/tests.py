from django.test import TestCase
from .models import Menu, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Ice Cream", price=5.00, inventory=10)
        itemstr = item.get_item()

        self.assertEqual(itemstr, "Ice Cream : 5.00")
