from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://advantageonlineshopping.com/#/")
    contact_us = page.get_by_role("CONTACT_US")
    select_cat = page.get_by_role("listbox")
    select_cat.click()


