from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class baseSeleniumDalya():

    def selenium_start(self):
        print("**test start**")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver


    def selenium_start_with_url(self, url: object) -> WebDriver:
        print("**test start**")
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        return self.driver

    def selenium_stop(self):
        print("**test stop**")
        self.driver.close()

    def click_and_assert_on_element(self, element: WebElement):
        print("clicking on element")
        is_selected = element.is_selected()
        if is_selected == False:
            element.click()
        after = element.is_selected()
        assert after == True, "After clicking on element is not as expected"
        return after

