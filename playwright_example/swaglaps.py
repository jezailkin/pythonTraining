from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    username = page.locator('#user-name')
    username.click()
    username.clear()
    username.fill("standard_user")

    password = page.locator('#password')
    password.click()
    password.clear()
    password.fill("secret_sauce")

    enter = page.locator('#login-button')
    enter.click()


    url = page.url
    assert url == "https://www.saucedemo.com/inventory.html"
    print("ok")
