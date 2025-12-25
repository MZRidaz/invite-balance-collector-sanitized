import os
import re
from playwright.sync_api import sync_playwright

def _block_resources(page):
    """
    Block unnecessary resources to speed up loading.
    """
    page.route(
        "**/*",
        lambda route, request: (
            route.abort()
            if request.resource_type in ["image", "font", "media"]
            else route.continue_()
        )
    )

def fetch_with_browser(p, browser, site):
    """
    Example site plugin demonstrating the recommended pattern:

    - headless-first scraping
    - automatic login detection
    - manual login fallback
    - persistent login state reuse (cookies / storage)

    This file is safe for GitHub:
    - No real site logic
    - No credentials
    - No private data
    """

    auth_file = f"auth/{site['name']}.json"
    raw_text = None
    need_login = False

    # ---------------------------
    # 1️⃣ Headless attempt
    # ---------------------------
    context = (
        browser.new_context(storage_state=auth_file)
        if os.path.exists(auth_file)
        else browser.new_context()
    )
    page = context.new_page()
    _block_resources(page)

    page.goto(site["invite_url"], wait_until="domcontentloaded")

    # Generic login detection (example logic)
    if (
        page.locator("input[type=password]").count() > 0
        or "login" in page.url.lower()
    ):
        need_login = True
    else:
        try:
            # Example selector, users should customize
            raw_text = page.locator("span.balance").first.inner_text(timeout=5000)
        except:
            need_login = True

    context.close()

    # ---------------------------
    # 2️⃣ Manual login fallback
    # ---------------------------
    if need_login:
        print(f"🔐 {site['name']} requires manual login")

        with sync_playwright() as p2:
            browser2 = p2.chromium.launch(headless=False)
            context2 = browser2.new_context()
            page2 = context2.new_page()
            _block_resources(page2)

            page2.goto(site["invite_url"], wait_until="load")

            input(
                "👉 Please complete login in the opened browser, "
                "confirm the page is ready, then press Enter"
            )

            os.makedirs("auth", exist_ok=True)
            context2.storage_state(path=auth_file)
            browser2.close()

    # ---------------------------
    # 3️⃣ Final headless scrape
    # ---------------------------
    context = browser.new_context(storage_state=auth_file)
    page = context.new_page()
    _block_resources(page)

    page.goto(site["invite_url"], wait_until="domcontentloaded")

    raw_text = page.locator("span.balance").first.inner_text(timeout=5000)
    context.close()

    value = re.sub(r"[^\d.]", "", raw_text)
    if not value:
        raise Exception(
            f"{site['name']} example failed to extract balance, "
            f"raw_text={raw_text!r}"
        )

    return float(value)
