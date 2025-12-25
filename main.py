from playwright.sync_api import sync_playwright
from config import SITES
import importlib
from excel_utils import ExcelWriter

def main():
    writer = ExcelWriter()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        for site in SITES:
            try:
                module = importlib.import_module(f"sites.{site['module']}")
                balance = module.fetch_with_browser(p, browser, site)

                print(f"✅ {site['name']} success: {balance}")
                writer.update(site["name"], balance)

            except Exception as e:
                print(f"❌ {site['name']} failed: {e}")

        browser.close()

    writer.save()
    print("\n=== All sites processed, Excel updated ===")

if __name__ == "__main__":
    main()
