from django.test import TestCase
from lists.forms import ItemForm,ExistingListItemForm,DUPLICATE_ITEM_ERROR,EMPTY_ITEM_ERROR
from lists.models import List, Item
# class ItemFormTest(TestCase):
#     def test_form_renders_item_text_input(self):
#         form = ItemForm()
#         # self.fail(form.as_p())
#         self.assertIn('placeholder="Enter a to-do item"', form.as_p())
#         self.assertIn('class="form-control input-lg"', form.as_p())
#
#     def test_form_validation_for_blank_items(self):
#         form = ItemForm(data={'text': ''})
#         # form.save()
#         self.assertFalse(form.is_valid())
#         self.assertEqual(
#             form.errors['text'],
#             ["You can't have an empty list item"]
#         )

class ExistingListItemFormTest(TestCase):
    def test_form_renders_item_text_input(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_)
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())

    def test_form_validation_for_blank_items(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_, data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'],[EMPTY_ITEM_ERROR])

    def test_form_validation_for_duplicate_items(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_,text = 'no twins')
        form = ExistingListItemForm(for_list=list_, data={'text': 'no twins'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'],DUPLICATE_ITEM_ERROR)