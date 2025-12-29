import unittest

from selenium.webdriver.common.by import By

from bershka_final_project.base_selenium_project import base_selenium_project


class product_page(unittest.TestCase):

    def setUp(self):
        self.base = base_selenium_project()
        self.driver = self.base.selenium_start_with_url("https://www.primark.com/en-gb")

    def tearDown(self):
        self.driver.close()


    def test_kids_page(self):
        accept_all = self.driver.find_element(By.ID,"onetrust-accept-btn-handler")
        accept_all.click()


        kids_page = self.driver.find_element(By.LINK_TEXT, "KIDS")
        kids_page.click()

        primark_page = self.driver.find_element(By.CLASS_NAME, "LinkedLogo-logoImage")
        primark_page.click()

        print("****test passed****")

