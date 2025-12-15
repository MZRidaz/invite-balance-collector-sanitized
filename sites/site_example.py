
from playwright.sync_api import sync_playwright
import re

def fetch(site):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(site['invite_url'])
        page.wait_for_selector("span.balance")
        text = page.locator("span.balance").first.inner_text()
        browser.close()
    return float(re.sub(r"[^\d.]", "", text))
