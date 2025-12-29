import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from bershka_final_project.base_selenium_project import base_selenium_project


class main_page(unittest.TestCase):

    def setUp(self):
        self.base = base_selenium_project()
        self.driver = self.base.selenium_start_with_url("https://www.bershka.com/es/en/h-woman.html")

    def tearDown(self):
        self.base.selenium_stop()

    def test_main_page(self):

        button_search = self.driver.find_element(By.CLASS_NAME, "top-bar-desktop__search-button")
        button_search.click()

        main_search = self.driver.find_element(By.CLASS_NAME, "input")
        main_search.click()
        main_search.send_keys("dress")
        main_search.send_keys(Keys.ENTER)

        price_all= self.driver.find_element(By.CLASS_NAME, "product-content")
        # print(price_all.text)

        index_1=price_all.text.index("€")
        index_2=price_all.text.index("dress")
        dress_price=price_all.text[index_1:index_2]
        dress_price=dress_price.strip()
        print(f"price is {dress_price}")