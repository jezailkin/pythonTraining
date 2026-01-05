from selenium.webdriver.common.by import By

from wolt_final_project.locaters import ELECTRONICS_STORE_PAGE


class Electronics_search:
    def __init__(self, driver):
        self.driver = driver


    def electorincs_stores_click(self):
        electronics_button = self.driver.find_element(*ELECTRONICS_STORE_PAGE.ELECTRONICS_BUTTON)
        electronics_button.click()

    def get_store_text(self):
        stores_options =self.driver.find_elements(*ELECTRONICS_STORE_PAGE.STORE_OPTIONS)[:6]
        # for store in stores_options:
        #     store.text
        # return stores_options

    # def get_store_information(self):
    #     store_open_until = self.driver.find_elements(By.CLASS_NAME,"v1b3l2om")[1]
    #     index_1 =store_open_until.text.index("Open")
    #     print (f"The store is  {store_open_until.text[index_1:]}")
    #
    #     min_order_price = self.driver.find_elements(By.CLASS_NAME,"v1b3l2om")[2]
    #     index_2 = min_order_price.text.index("₪") +1
    #     price= float(min_order_price.text[index_2:])
    #     if price > 40:
    #         print(f"Min order price is  {price} ")