import unittest

from selenium.webdriver.common.by import By

from selenium_example.baseSeleniumDalya import baseSeleniumDalya


class zara (unittest.TestCase):


    def setUp(self):
        self.base = baseSeleniumDalya()
        self.driver= self.base.selenium_start_with_url("https://www.zara.com/il/en/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_search(self):
        search = self.driver.find_element(By.CLASS_NAME, "layout-header-action-search__content")
        search.click()
        print ("******test passed*****")


    def test_shopping_bag(self):
        shopping_bag = self.driver.find_element(By.PARTIAL_LINK_TEXT,"SHOPPING BAG")
        shopping_bag_text =shopping_bag.text
        is_pass='[0]' in shopping_bag_text
        assert is_pass,"shopping bag is not empty"
        print("******test passed*****")