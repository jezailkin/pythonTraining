import time
import unittest

from wolt_final_project.globals import HOME_PAGE, DISCOVERY_PAGE, TEXT_EXIST, WORD_FOUND, FIRST_WORD_FOUND, \
    FIRST_BUTTON, SECOND_BUTTON, THIRD_BUTTON
from wolt_final_project.pages.electronic_store_page import Electronics_search
from wolt_final_project.pages.mac_restaurant_page import Mac_restaurants
from wolt_final_project.pages.main_page import Main_page
from wolt_final_project.pages.search_page import Search_page
from wolt_final_project.pages.wolt_word_page import Wolt_icon
from wolt_final_project.tests.baseSeleniumwolt import seleniumBaseWolt


class allTests(unittest.TestCase):


    def setUp(self):
        self.base =  seleniumBaseWolt()
        self.driver = self.base.selenium_start_with_url("https://wolt.com/en/isr")
        self.base.click_on_allow_botton()
        self.base.select_city()
        self.main_page = Main_page(self.driver)
        self.wolt_word_page= Wolt_icon(self.driver)
        self.electronic_store_page= Electronics_search(self.driver)
        self.mac_restaurants_page = Mac_restaurants(self.driver)
        self.search_page = Search_page(self.driver)



    def tearDown(self):
        self.base.selenium_stop()



    def test_check_amount_of_restaurants(self):
        self.main_page.store_type_click()
        self.main_page.check_for_restaurants_amount()

        text_option=self.main_page.get_rest_option()
        assert TEXT_EXIST in text_option, "unexpected text."
        print(f"the word *burger* was found in {text_option}")



    def test_back_to_main_page_by_word_wolt(self):
        time.sleep(3)
        url1 = self.driver.current_url
        assert url1 == DISCOVERY_PAGE
        print(url1)
        self.wolt_word_page.back_to_main_page()
        url2 = self.driver.current_url
        assert url2 == HOME_PAGE
        print(url2)



    def test_get_electronics_word(self):
        self.electronic_store_page.electorincs_stores_click()
        stores_list= self.electronic_store_page.get_store_text()
        for store in stores_list:
            assert WORD_FOUND in store, "unexpected text."




    def test_first_option_is_mac(self):
        self.mac_restaurants_page.rest_search_click()
        first_rest_option= self.mac_restaurants_page.get_first_option()
        assert FIRST_WORD_FOUND in first_rest_option , "unexpected text was found in the first search option."
        print(f"first restaurant found: {first_rest_option}")



    def test_check_if_buttons_exist(self):
        discovery_word=self.search_page.searching_for_button_discovery()
        assert FIRST_BUTTON in discovery_word, "unexpected text."
        print(f"first button found: {discovery_word}")


        restaurants_word=self.search_page.searching_for_button_restaurants()
        assert SECOND_BUTTON in restaurants_word, "unexpected text."
        print(f"second button found: {restaurants_word}")


        stores_word=self.search_page.searching_for_button_stores()
        assert THIRD_BUTTON in stores_word, "unexpected text."
        print(f"third button found: {stores_word}")

