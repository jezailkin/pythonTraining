from selenium.webdriver.common.by import By

from selenium_example.baseSeleniumDalya import baseSeleniumDalya

base= baseSeleniumDalya()
exp_link ="payment calculator"
driver=base.selenium_start_with_url("https://www.calculator.net/")
Buttons=driver.find_elements(By.PARTIAL_LINK_TEXT,"Calculator")
math_button = driver.find_elements(By.LINK_TEXT,"Math")
if len(math_button)>0:
    math_button.click()
number_of_buttons =len(Buttons)
for button in Buttons:
    index = Buttons.index(button)
    print(f"{button.text} found at  index {index}")
    if (button.text==exp_link):
        print(f"####{button.text} found at  index {index}####")


base.selenium_stop()
