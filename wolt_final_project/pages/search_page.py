from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Search_page:
    def __init__(self, driver):
        self.driver = driver


    def searching_for_button_discovery(self):
        discovery_button = self.driver.find_elements(By.CLASS_NAME, "sysyh6h")[0]
        text_1=discovery_button.text
        return text_1


    def searching_for_button_restaurants(self):
        restaurants_button = self.driver.find_elements(By.CLASS_NAME, "sysyh6h")[1]
        text_2=restaurants_button.text
        return text_2



    def searching_for_button_stores(self):
        stores_button = self.driver.find_elements(By.CLASS_NAME, "sysyh6h")[2]
        text_3=stores_button.text
        return text_3
