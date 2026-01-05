from selenium.webdriver.common.by import By


class MAC_RESTAURANT_PAGE:
    SEARCH_BOX =(By.CLASS_NAME, "i131pb3d")
    FIRST_RES=(By.CSS_SELECTOR, 'a[data-test-id="venueCard.mac-david"]')


class ELECTRONICS_STORE_PAGE:
    ELECTRONICS_BUTTON =(By.PARTIAL_LINK_TEXT, "Electronics")
    STORE_OPTIONS=(By.CLASS_NAME, "d1r05llc.dgyvenz")

class MAIN_PAGE:
    RESTAURANT_OPTION = (By.PARTIAL_LINK_TEXT, "Restaurants")
    BURGER_REST=(By.PARTIAL_LINK_TEXT, "Burger")


class SEARCH_PAGE:
    DISCOVERY_BUTTON = (By.CLASS_NAME, "sysyh6h")
    RESTAURANT_BUTTON = (By.CLASS_NAME, "sysyh6h")
    STORES_BUTTON = (By.CLASS_NAME, "sysyh6h")

class WOLT_WORD_PAGE:
    WOLT_WORD_ICON = (By.ID, "lottie")


