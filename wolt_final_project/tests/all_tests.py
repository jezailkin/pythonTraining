import time
import unittest

from wolt_final_project.pages.electronic_store_page import Electronics_search
from wolt_final_project.pages.mac_restaurant_page import Mac_restaurants
from wolt_final_project.pages.main_page import Main_page
from wolt_final_project.pages.search_page import Search_page
from wolt_final_project.pages.wolt_word_page import Wolt_word
from wolt_final_project.tests.baseSeleniumwolt import seleniumBaseWolt


class allTests(unittest.TestCase):


    def setUp(self):
        self.base =  seleniumBaseWolt()
        self.driver = self.base.selenium_start_with_url("https://wolt.com/en/isr")
        self.base.click_on_allow_botton()
        self.base.select_city()
        self.main_page = Main_page(self.driver)
        self.wolt_word_page= Wolt_word(self.driver)
        self.electronic_store_page= Electronics_search(self.driver)
        self.mac_restaurants_page = Mac_restaurants(self.driver)
        self.search_page = Search_page(self.driver)



    def tearDown(self):
        self.base.selenium_stop()



    def test_check_amount_of_restaurants(self):
        self.main_page.store_type()
        self.main_page.if_there_is_more_than_one_burger_restaurant()

        text_option=self.main_page.rest_option()
        assert "Burger" in text_option, "unexpected text."
        print(f"the word *burger* was found in {text_option}")



    def test_back_to_main_page_by_word_wolt(self):
        time.sleep(3)
        url1 = self.driver.current_url
        assert url1 == "https://wolt.com/en/discovery"
        print(url1)
        self.wolt_word_page.back_to_main_page()
        url2 = self.driver.current_url
        assert url2 == "https://wolt.com/en/isr"
        print(url2)



    def test_info_for_first_electronics_search_option(self):
   4     self.electronic_store_page.electorincs_stores()



    def test_first_option_is_mac(self):
        self.mac_restaurants_page.mac_rest_search()
        first_rest_option= self.mac_restaurants_page.first_option_apppears()
        assert "Mac" in first_rest_option , "unexpected text was found in the first search option."
        print(f"first restaurant found: {first_rest_option}")



    def test_check_if_buttons_exist(self):
        discovery_word=self.search_page.searching_for_button_discovery()
        assert "Discovery" in discovery_word, "unexpected text."
        print(f"first button found: {discovery_word}")


        restaurants_word=self.search_page.searching_for_button_restaurants()
        assert "Restaurants" in restaurants_word, "unexpected text."
        print(f"second button found: {restaurants_word}")


        stores_word=self.search_page.searching_for_button_stores()
        assert "Stores" in stores_word, "unexpected text."
        print(f"third button found: {stores_word}")