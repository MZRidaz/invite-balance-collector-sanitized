![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Playwright](https://img.shields.io/badge/playwright-supported-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)

# Invite Balance Collector

---

## English

Invite Balance Collector is a **Playwright-based automation framework** for collecting  
invite / referral wallet balances from multiple websites and aggregating them into Excel.

This project is designed for **real-world websites that require authentication**,  
and provides a **safe and stable login handling strategy**.

---

### ✨ Features

- Modular **site plugin architecture**
- Playwright browser automation
- Excel aggregation output
- Windows / Linux support
- **Headless-first scraping**
- **Automatic manual-login fallback**
- Persistent login state (cookies & storage)
- Safe for GitHub (no secrets included)

---

### 🔐 Authentication Strategy (Important)

Some target websites require authentication.

This project uses a **headless-first with manual-login fallback** strategy:

1. The script first tries to scrape using **headless mode**
2. If the site is **not logged in**:
   - A browser window automatically opens
   - You complete login **manually**
   - Login state is saved (cookies / storage)
3. Subsequent runs reuse the saved login state  
   → **No need to log in again unless the session expires**

This approach is:
- Safer than hardcoding credentials
- More stable against site changes
- Commonly used in production automation systems

---

### 🛠 Installation

```bash
pip install -r requirements.txt
playwright install
