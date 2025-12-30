
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class Main_page:
    def __init__(self, driver):
        self.driver = driver


    def store_type(self):
        restaurants= (self.driver.find_element(By.LINK_TEXT,"Restaurants"))
        restaurants.click()

    def rest_option(self):
        burger= self.driver.find_element(By.PARTIAL_LINK_TEXT, "Burger")
        butger_text= burger.text
        return butger_text


    def if_there_is_more_than_one_burger_restaurant(self):
        burger= self.driver.find_element(By.PARTIAL_LINK_TEXT, "Burger")
        burger1= burger.text.split()
        for i in range(len(burger1)):
            if burger1 [i]=="places":
                text_int=int(burger1[i-1])
                # print(text_int)
                if text_int > 1:
                    print (f"there is {text_int} places sell burgers ")
                else :
                    print (f"there is no burger places ")
                return