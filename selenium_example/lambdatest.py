from selenium.webdriver.common.by import By

from selenium_example.baseSeleniumDalya import baseSeleniumDalya

base = baseSeleniumDalya()
driver = base.selenium_start_with_url("https://ecommerce-playground.lambdatest.io/")
elements = driver.find_elements(By.CLASS_NAME,"figure-img.img-fluid.lazy-load")
windows_button = elements[0]
windows_button.click()

prices = driver.find_elements(By.CLASS_NAME,"price-new")
for price in prices:
    print(price.text)

base.selenium_stop()
