import unittest

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


        Enter_delivery_address = self.driver.find_element(By.ID, "_R_tdj_")
        Enter_delivery_address.click()
        Enter_delivery_address.send_keys("Haifa")
        Enter_delivery_address.send_keys(Keys.RETURN)
        haifa_button= self.driver.find_element(By.CLASS_NAME,"sac3j8c")
        haifa_button.click()

        restaurants= (self.driver.find_element(By.LINK_TEXT,"Restaurants"))
        restaurants.click()


        burger= self.driver.find_elements(By.CLASS_NAME,"b1htiduy")[2]
        print(burger)
        burger1= burger.text.split()
        for i in range(len(burger1)):
            if burger1 [i]=="places":
                text_int=int(burger1[i-1])
                print(text_int)
                if text_int > 1:
                    print (f"there is {text_int} burger places ")
                else :
                    print (f"there is no burger places ")
                return

