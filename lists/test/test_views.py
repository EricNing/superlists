from django.utils.html import escape
from django.test import TestCase
from lists.models import List,Item
# class NewListTest(TestCase):
#     def test_validation_errors_are_sent_back_to_home_page_template(self):
#         response = self.client.post('/lists/new', data={'item_text': ''})
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'lists/home.html')
#         excepted_error = escape("You can't have an empty list item")
#         # excepted_error = "You can&#39;t have an empty list item"
#         # print(response.content.decode())
#         self.assertContains(response, excepted_error)

# class ListViewTest(TestCase):
#     def test_can_save_a_POST_request_to_an_existing_list(self):
#         other_list = List.objects.create()
#         correct_list = List.objects.create()
#
#         self.client.post(
#             f'/lists/{correct_list.id}/',
#             data={'item_text': 'A new item for an existing list'}
#         )
#         self.assertEqual(Item.objects.count(), 1)
#         new_item = Item.objects.first()
#         self.assertEqual(new_item.text, 'A new item for an existing list')
#         self.assertEqual(new_item.list, correct_list)
#
#     def test_POST_redirects_to_list_view(self):
#         other_list = List.objects.create()
#         correct_list = List.objects.create()
#
#         response = self.client.post(
#             f'/lists/{correct_list.id}/',
#             data={'item_text': 'A new item for an existing list'}
#         )
#         self.assertRedirects(response, f'/lists/{correct_list.id}/')
#
#     def test_validation_errors_end_up_on_lists_page(self):
#         list_ = List.objects.create()
#         response = self.client.post(
#             f'/lists/{list_.id}/',
#             data={'item_text': ''}
#         )
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'lists/list.html')
#         expected_error = escape("You can't have an empty list item")
#         self.assertContains(response, expected_error)