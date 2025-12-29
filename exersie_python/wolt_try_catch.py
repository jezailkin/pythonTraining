import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium_example.baseSeleniumDalya import baseSeleniumDalya


class wolt_try_catch(unittest.TestCase):

    def setUp(self):
            self.base = baseSeleniumDalya()
            self.driver = self.base.selenium_start_with_url("https://wolt.com/en/isr")

    def tearDown(self):
            self.base.selenium_stop()

    def test_wolt_try_catch(self):
        search = self.driver.find_element(By.ID, "_R_tdj_")
        search.click()
        search.send_keys("burger")
        search.send_keys(Keys.RETURN)