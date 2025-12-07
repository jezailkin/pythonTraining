import time
from time import sleep
from xml.sax.handler import feature_namespace_prefixes

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

print("Test start")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://demoqa.com/login')

driver.find_element(By.ID,"userName")
user.click()
user.send_keys("ffff")


password = driver.find_element(By.NAME, "password")
password.send_keys("qqwqwqwqwqw")
driver.close()