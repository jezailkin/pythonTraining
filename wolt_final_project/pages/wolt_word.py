import time
import unittest
from re import search

import self
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from wolt_final_project.tests.baseSeleniumwolt import seleniumBaseWolt


class main_page(unittest.TestCase):

    def setUp(self):
        self.base =seleniumBaseWolt()
        self.driver = self.base.selenium_start_with_url("https://wolt.com/en/isr")

    def tearDown(self):
        self.driver.close()

    def test_main_page(self):
        allow = self.driver.find_element(By.CSS_SELECTOR, "button[data-test-id='allow-button']")
        allow.click()

        enter_delivery_address = self.driver.find_element(By.ID, "_R_tdj_")
        enter_delivery_address.click()
        enter_delivery_address.send_keys("Haifa")
        enter_delivery_address.send_keys(Keys.ENTER)
        # search_button= self.driver.find_element(By.CLASS_NAME,"wpt-ui-RoundedInput_IconButtonWrapper_iyz9630")
        # search_button.click()
        time.sleep(3)
        url = self.driver.current_url
        assert url == "https://wolt.com/en/discovery", "Unexpected url."