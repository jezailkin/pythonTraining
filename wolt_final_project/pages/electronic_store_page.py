from selenium.webdriver.common.by import By


class Electronics_search:
    def __init__(self, driver):
        self.driver = driver


    def electorincs_stores(self, store_type="Electronics"):
        electronics_button = self.driver.find_element(By.PARTIAL_LINK_TEXT, store_type)
        electronics_button.click()
        first_6_store_options =self.driver.find_element(By.CLASS_NAME, "d1r05llc.dgyvenz")(0,5)
        print(first_6_store_options.text)



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