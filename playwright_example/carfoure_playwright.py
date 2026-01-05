from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.carrefour.com/en")
    accept_coockies = page.locator('#onetrust-accept-btn-handler')
    accept_coockies.click()

    stores_button= page.get_by_text('Diversity')
    assert stores_button.text_content()
    print("Success!")


