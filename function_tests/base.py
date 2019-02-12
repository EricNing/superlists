from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def wait_for_row_in_list_table(self, row_text):
        pass