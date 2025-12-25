![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Playwright](https://img.shields.io/badge/playwright-supported-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)

# Invite Balance Collector

Invite Balance Collector is a **Playwright-based automation tool** for collecting  
invite / referral wallet balances from multiple websites and aggregating them into Excel.

It is designed for **real-world websites that require authentication**.

---

## ✨ Features

- Modular **site plugin architecture**
- Playwright browser automation (sync API)
- **Headless-first scraping**
- **Automatic manual-login fallback**
- Persistent login state (cookies & storage)
- **Batch Excel writing (open once, save once)**
- Windows / Linux support
- Safe for GitHub (no credentials included)

---

## 🔐 Authentication Strategy

This project uses a **headless-first with manual-login fallback** approach:

- Tries to scrape using headless mode
- If login is required:
  - A browser window opens
  - You log in manually once
  - Login state is saved and reused
- No need to log in again unless the session expires

This avoids hardcoded passwords and is more stable for long-term use.

---

## ⚡ Performance

- Playwright initialized once per run
- Single browser instance reused
- Isolated browser contexts per site
- Images, fonts, and media blocked
- Excel file written **once per run**

---

## 🛠 Installation

```bash
pip install -r requirements.txt
playwright install
```

---

## ▶ Usage

### 1️⃣ Create config

```bash
cp config.example.py config.py
```

Edit `config.py`:

```python
SITES = [
    {
        "name": "site_example",
        "invite_url": "https://example.com/invite",
        "module": "site_example"
    }
]
```

---

### 2️⃣ Run

```bash
python main.py
```

- Logged in → runs headless
- Not logged in → browser opens for manual login

---

## 🧩 Site Plugin Interface

Each site plugin must implement:

```python
def fetch_with_browser(p, browser, site: dict) -> float:
    ...
```

Rules:

- One site = one plugin
- Filename must match `site["module"]`
- Return a numeric value (`float`)
- Do not hardcode credentials

---

## 📊 Excel Output

Default file: `excel/invite_balance.xlsx`

| Website | Current Balance | Last Update Time | Remark |
|--------|-----------------|------------------|--------|

Data is written in batch and saved once.

---

## 🔒 Security

Do NOT commit:

- `config.py`
- `auth/*.json`
- Real credentials
- Excel files with real data

---

## 📜 License

MIT License.

---

## 🙌 Contributing

Contributions are welcome.  
See `CONTRIBUTING.md` for details.