import time
import unittest

from requests import URLRequired
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium_example.baseSeleniumDalya import baseSeleniumDalya


class calculator__1(unittest.TestCase):

    def setUp(self):
        self.base= baseSeleniumDalya()
        self.driver = self.base.selenium_start_with_url("https://www.calculator.net/interest-calculator.html")

    def tearDown(self):
        self.base.selenium_stop()

    def test_clear_button_text(self):
        self.driver.find_element(By.NAME,"cstartingprinciple").clear()
        # self.driver.find_element(By.NAME,"cannualaddition").clear()
        # self.driver.find_element(By.NAME,"cmonthlyaddition").clear()
        # self.driver.find_element(By.NAME,"cinterestrate").clear()
        self.driver.find_element(By.NAME,"ctaxtrate").clear()

        initial_investment = self.driver.find_element(By.ID, "cstartingprinciple")
        initial_investment.click()
        initial_investment.send_keys(2000)

        initial_investment = self.driver.find_element(By.ID, "ctaxtrate")
        initial_investment.click()
        initial_investment.send_keys(40000)

        radio= self.driver.find_element(By.CLASS_NAME,"rbmark")
        radio.click()

        Compound = self.driver.find_element(By.NAME, "ccompound")
        Compound_as_dropdown = Select(Compound)
        Compound_as_dropdown.select_by_index(2)

        calculate= self.driver.find_element(By.NAME, "x")
        calculate.click()

        print_button =self.driver.find_element(By.LINK_TEXT, "Print")
        time.sleep (4)
        print_button.is_displayed()
        assert print_button.is_displayed(),"print_button not displayed"


