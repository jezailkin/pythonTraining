from selenium.webdriver.common.by import By

from selenium_example.baseSeleniumDalya import baseSeleniumDalya

base = baseSeleniumDalya()
# driver = base.selenium_start()
#
# driver.get("https://www.nike.com/il/")
driver = base.selenium_start_with_url("https://www.nike.com/il/")

woman_text =driver.find_element(By.LINK_TEXT,"Women").text
driver.find_element(By.PARTIAL_LINK_TEXT, "Find").click()

url = driver.current_url
print(url)

if (url == 'https://www.nike.com/il/retail'):
    print("Test OK - URL as expected")

else:
    print("#####Test FAILED - URL not as expected######")

base.selenium_stop()

