from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class seleniumBaseWolt():


    def selenium_start_with_url(self, url):
        print("**** Test start ****")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        return self.driver

    def selenium_stop(self):
        print("**** Test stop ****")
        self.driver.close()

    def click_on_allow_botton(self):
        print("**** Test allow botton ****")
        allow_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-test-id='allow-button']")
        allow_button.click()

    def select_city(self, city="Haifa"):
        print("**** Test select city ****")
        Enter_delivery_address = self.driver.find_element(By.ID, "_R_tdj_")
        Enter_delivery_address.click()
        Enter_delivery_address.send_keys(city)
        Enter_delivery_address.send_keys(Keys.RETURN)
        haifa_button = self.driver.find_element(By.CLASS_NAME, "sac3j8c")
        haifa_button.click()

