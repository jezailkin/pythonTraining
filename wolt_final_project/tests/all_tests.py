import unittest

from wolt_final_project.pages.main_page import main_page
from wolt_final_project.tests.baseSeleniumwolt import seleniumBaseWolt


class allTests(unittest.TestCase):


    def setUp(self):
        self.base =  seleniumBaseWolt()
        self.driver = self.base.selenium_start_with_url("https://www.primark.com/en-gb")
        self.main_page = main_page(self.driver)

    def tearDown(self):
        self.base.selenium_stop()



    def test_click_on_search_button(self):
        search_button = self.main_page.click_button_and_get_text("Enter delivery address")
        assert search_button  ==()

    def test_click_on_cart_button(self):
        self.main_page.click_on_cart_button()
        self.cart_page.get_cart_message()