import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium_example.baseSeleniumDalya import baseSeleniumDalya


class nike_getting_price(unittest.TestCase):

    def setUp(self):
        self.base = baseSeleniumDalya()
        self.driver = self.base.selenium_start_with_url("https://www.nike.com/il/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_second_shoe_price(self):

        search = self.driver.find_element(By.ID, "gn-search-input")
        search.click()
        search.send_keys("shoes")
        search.send_keys(Keys.ENTER)

        second_shoes = self.driver.find_element(By.CLASS_NAME, "product-card__body")
        second_shoes.click()
        price= self.driver.find_element(By.CLASS_NAME, "css-e4uzb4")
        price = float([price]).strip("₪")
        print (price)
        # print(print_price.text)

        # assert price +10 ,"add 10%"
        # print(price)


