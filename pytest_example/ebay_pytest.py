import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium_example.baseSeleniumDalya import baseSeleniumDalya
from selenium_example.ebay import url


class ebay_pytest(unittest.TestCase):

    def setUp(self):
        self.base= baseSeleniumDalya()
        self.driver = self.base.selenium_start_with_url("https://www.ebay.com/")

    def tearDown(self):
        self.base.selenium_stop()


    def test_keyboard_as_dropdown(self):
        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()

        enter_keyboards = self.driver.find_element(By.ID, "_nkw")
        enter_keyboards.send_keys("shirt")

        keyboard_options = self.driver.find_element(By.NAME, "_in_kw")
        keyboard_options_as_dropdown=Select(keyboard_options)
        keyboard_options_as_dropdown.select_by_index(2)

        check_box = self.driver.find_element(By.ID, "s0-1-20-5[1]-[0]-LH_TitleDesc")
        check_box.click()

        radio = self.driver.find_element(By.ID,"s0-1-20-6[3]-[0]-LH_BO")
        radio.click()

        enter_keyboards.send_keys(Keys.ENTER)

        url = self.driver.current_url
        # assert url =="https://www.ebay.com/sch/i.html?_nkw=shirt"