from selenium.webdriver.common.by import By

from selenium_example.baseSeleniumDalya import baseSeleniumDalya

base= baseSeleniumDalya()

driver=base.selenium_start_with_url("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

login_button=driver.find_element(By.CLASS_NAME,"btn.btn-primary.btn-lg")
login_button.click()

base.selenium_stop()

