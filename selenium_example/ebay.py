from selenium.webdriver.common.by import By

from selenium_example.baseSeleniumDalya import baseSeleniumDalya

base = baseSeleniumDalya()
driver = base.selenium_start()


driver.get('https://www.ebay.com/')


advanced_text= driver.find_element(By.LINK_TEXT,"Advanced").text

if advanced_text=="Advanced":
    driver.find_element(By.LINK_TEXT, "Advanced").click()
    url= driver.current_url
    print(url)

driver.close()
