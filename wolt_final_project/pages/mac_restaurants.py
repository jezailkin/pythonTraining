
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Mac_restaurants:
    def __init__(self, driver):
        self.driver = driver


    def mac_search(self,rest="mac"):
        search_box= self.driver.find_element(By.CLASS_NAME, "i131pb3d")
        search_box.click()
        search_box.send_keys(rest)
        search_box.send_keys(Keys.ENTER)

    def first_option(self):
        first_res = self.driver.find_elements(By.CSS_SELECTOR, 'a[data-test-id="venueCard.mac-david"]')        # text = first_res[0].text
        text = first_res[0].text
        return text
