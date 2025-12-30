from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Electronics_search:
    def __init__(self, driver):
        self.driver = driver


    # def select_city(self, city="Haifa"):
    #     Enter_delivery_address = self.driver.find_element(By.ID, "_R_tdj_")
    #     Enter_delivery_address.click()
    #     Enter_delivery_address.send_keys(city)
    #     Enter_delivery_address.send_keys(Keys.RETURN)
    #     haifa_button = self.driver.find_element(By.CLASS_NAME, "sac3j8c")
    #     haifa_button.click()

    def electorincs_first_store(self):
        electronics = self.driver.find_element(By.LINK_TEXT, "Electronics")
        electronics.click()
        first_store =self.driver.find_element(By.CLASS_NAME, "blr9pzd")
        first_store.click()


    def store_information(self):
        open_until = self.driver.find_elements(By.CLASS_NAME,"v1b3l2om")[1]
        index_1 =open_until.text.index("until ")+5
        print (f"is open till {open_until.text[index_1:]}")

        min_order = self.driver.find_elements(By.CLASS_NAME,"v1b3l2om")[2]
        index_2 = min_order.text.index("₪") +1
        price= float(min_order.text[index_2:])
        if price > 40:
            print(f"Min order is  {price} ")