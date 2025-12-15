
from config import SITES, EXCEL_FILE
import importlib

for site in SITES:
    module = importlib.import_module(f"sites.{site['module']}")
    balance = module.fetch(site)
    print(site['name'], balance)
