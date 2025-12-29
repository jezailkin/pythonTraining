import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from unicodedata import category

from selenium_example.baseSeleniumDalya import baseSeleniumDalya


class pytset_adv_demo(unittest.TestCase):




    def setUp(self):
        self.base= baseSeleniumDalya()
        self.driver=self.base.selenium_start_with_url("https://advantageonlineshopping.com/#/")
    def tearDown(self):
        self.base.selenium_stop()


    def test_dropdown_example(self):
        print("start test for dropdown example")
        time.sleep(5)
        contact_us= self.driver.find_element(By.LINK_TEXT,"CONTACT US")
        contact_us.click()
        category=self.driver.find_element(By.NAME,"categoryListboxContactUs")
        category_as_dropdown=Select(category)

        category_as_dropdown.select_by_index(2)
        category_as_dropdown.select_by_visible_text("Mice")
        print("into test")

        


