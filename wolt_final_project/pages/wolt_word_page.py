
from selenium.webdriver.common.by import By

class Wolt_word:
    def __init__(self, driver):
        self.driver = driver




    def back_to_main_page(self):
        wolt_word_icon = self.driver.find_element(By.ID, "lottie")
        wolt_word_icon.click()
