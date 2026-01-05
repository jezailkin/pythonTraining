from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.calculator.net/")
    bmi_Calculator= page.get_by_role("BMI_Calculator")
    bmi_Calculator.click()