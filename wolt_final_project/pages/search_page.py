from wolt_final_project.locaters import SEARCH_PAGE


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def searching_for_button_discovery(self):
        discovery_button = self.driver.find_elements(*SEARCH_PAGE.DISCOVERY_BUTTON)[0]
        discovery_text=discovery_button.text
        return discovery_text


    def searching_for_button_restaurants(self):
        restaurants_button = self.driver.find_elements(*SEARCH_PAGE.RESTAURANT_BUTTON)[1]
        restaurant_text=restaurants_button.text
        return restaurant_text



    def searching_for_button_stores(self):
        stores_button = self.driver.find_elements(*SEARCH_PAGE.STORES_BUTTON)[2]
        stores_text=stores_button.text
        return stores_text
