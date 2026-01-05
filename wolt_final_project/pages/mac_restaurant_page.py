
from selenium.webdriver import Keys

from wolt_final_project.locaters import MAC_RESTAURANT_PAGE


class Mac_restaurants:
    def __init__(self, driver):
        self.driver = driver


    def rest_search_click(self, rest="mac"):
        search_box= self.driver.find_element(*MAC_RESTAURANT_PAGE.SEARCH_BOX)
        search_box.click()
        search_box.send_keys(rest)
        search_box.send_keys(Keys.ENTER)

    def get_first_option(self):
        first_res = self.driver.find_elements(*MAC_RESTAURANT_PAGE.FIRST_RES)
        text = first_res[0].text
        return text
