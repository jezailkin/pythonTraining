from wolt_final_project.locaters import MAIN_PAGE


class Main_page:
    def __init__(self, driver):
        self.driver = driver

    def back_to_main_page(self):
        wolt_word_icon = self.driver.find_element(*MAIN_PAGE.WOLT_WORD_ICON)
        wolt_word_icon.click()

    def store_type_click(self):
        restaurants_option= self.driver.find_element(*MAIN_PAGE.RESTAURANT_OPTION)
        restaurants_option.click()


    def check_for_restaurants_amount(self):
        burger_rest= self.driver.find_element(*MAIN_PAGE.BURGER_REST)
        burger_text= burger_rest.text.split()
        for i in range(len(burger_text)):
            if burger_text[i]=="places":
                text_int=int(burger_text[i-1])
                if text_int > 1:
                    print (f"there is {text_int} places sell burgers ")
                else :
                    print (f"there is no burger places ")
                return


    def get_rest_option(self):
        burger_rest= self.driver.find_element(*MAIN_PAGE.BURGER_REST)
        burger_rest_text= burger_rest.text
        return burger_rest_text