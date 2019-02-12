from django.core.exceptions import ValidationError
from django.test import TestCase
from lists.models import List, Item
# class ListAndItemModelsTest(TestCase):
#     def test_cannot_save_empty_list_imtes(self):
#         list_ = List.objects.create()
#         item = Item(list=list_, text='')
#         with self.assertRaises(ValidationError):
#             item.save()
#             item.full_clean()