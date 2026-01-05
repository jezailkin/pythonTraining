from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://blazedemo.com/")
    select_country = page.locator("[name='fromPort']")
    select_country.select_option("Paris")
    select_city_destination = page.locator("[name='toPort']")
    select_city_destination.select_option("Cairo")
    find_flight=page.locator("[value='Find Flights']")
    find_flight.click()


