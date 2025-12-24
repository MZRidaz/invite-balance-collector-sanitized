from playwright.sync_api import sync_playwright
import re
import os

def fetch(site):
    """
    Example site plugin demonstrating:
    - headless-first scraping
    - automatic detection of login requirement
    - manual login fallback
    - persistent login state (cookies)

    site dict example:
    {
        "name": "site_example",
        "invite_url": "https://example.com/invite",
        "module": "site_example"
    }
    """

    auth_file = f"auth/{site['name']}.json"
    raw_text = None
    need_login = False

    # ---------- Step 1: Try headless scraping ----------
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        context = (
            browser.new_context(storage_state=auth_file)
            if os.path.exists(auth_file)
            else browser.new_context()
        )

        page = context.new_page()
        page.goto(site["invite_url"], wait_until="domcontentloaded")
        page.wait_for_timeout(2000)

        # Generic login detection (example logic)
        if (
            page.locator("input[type=password]").count() > 0
            or "login" in page.url.lower()
        ):
            need_login = True
        else:
            try:
                raw_text = page.locator("span.balance").first.inner_text(timeout=3000)
            except:
                need_login = True

        browser.close()

    # ---------- Step 2: Manual login if required ----------
    if need_login:
        print(f"🔐 {site['name']} requires manual login")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            page.goto(site["invite_url"], wait_until="load")
            input("👉 Please complete login in the opened browser, then press Enter")

            os.makedirs("auth", exist_ok=True)
            context.storage_state(path=auth_file)
            browser.close()

    # ---------- Step 3: Headless scraping with saved login ----------
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(storage_state=auth_file)
        page = context.new_page()

        page.goto(site["invite_url"], wait_until="domcontentloaded")
        page.wait_for_timeout(2000)

        raw_text = page.locator("span.balance").first.inner_text()
        browser.close()

    value = re.sub(r"[^\d.]", "", raw_text)
    if not value:
        raise Exception(
            f"{site['name']} example failed to extract balance, raw_text={raw_text!r}"
        )

    return float(value)
