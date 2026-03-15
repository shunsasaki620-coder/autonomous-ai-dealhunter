from __future__ import annotations

import sys
import os
import time

# Ensure repo root is on sys.path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from ..tools.mercari_scanner import scan_mercari
from ..pipelines.deal_analyzer import analyze_deals
from ..memory.deal_memory import filter_new_deals


BRANDS = [
    "patagonia",
    "carhartt",
    "arc'teryx",
    "north face"
]


def run_monitor():

    while True:

        print("\n============================")
        print("Scanning marketplace...")
        print("============================\n")

        all_items = []

        for brand in BRANDS:

            print("Searching:", brand)

            items = scan_mercari(brand)

            new_items = filter_new_deals(items)

            print("New listings found:", len(new_items))

            all_items.extend(new_items)

        print("\nItems scraped:", len(all_items))

        if not all_items:
            print("No new listings found.")
            print("Next scan in 5 minutes...\n")
            time.sleep(300)
            continue

        deals = analyze_deals(all_items)

        print("\n🔥 Best deals found:\n")

        for deal in deals[:5]:

            print("🔥 DEAL")
            print("Item:", deal["title"])
            print("Price:", deal["price"])
            print("Resale:", deal["resale"])
            print("Profit:", deal["profit"])
            print()

        print("Next scan in 5 minutes...\n")

        time.sleep(300)


if __name__ == "__main__":
    run_monitor()