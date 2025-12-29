import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium_example.baseSeleniumDalya import baseSeleniumDalya


class ebay_search_cost(unittest.TestCase):

        def setUp(self):
            self.base = baseSeleniumDalya()
            self.driver = self.base.selenium_start_with_url("https://www.ebay.com/")

        def tearDown(self):
            self.base.selenium_stop()

        def test_ebay_search_cost(self):
            search= self.driver.find_element(By.ID, "gh-ac")
            search.click()
            search.send_keys("backbag")
            search_button= self.driver.find_element(By.ID, "gh-search-btn")
            search_button.click()
            price_all = self.driver.find_element(By.CLASS_NAME,"su-card-container__attributes.su-card-container__attributes--has-secondary")
            print(price_all.text)

            index_1=price_all.text.index("+ILS")+4
            index_2=price_all.text.index("delivery")
            delivery_price=price_all.text[index_1:index_2]
            delivery_price=delivery_price.strip()
            print(delivery_price)

