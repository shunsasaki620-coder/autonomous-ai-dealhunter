import json
import os

DATA_FILE = "data/seen_deals.json"


def load_seen_deals():
    if not os.path.exists(DATA_FILE):
        return set()

    with open(DATA_FILE, "r") as f:
        return set(json.load(f))


def save_seen_deals(deals):
    with open(DATA_FILE, "w") as f:
        json.dump(list(deals), f)


def filter_new_deals(items):
    seen = load_seen_deals()

    new_items = []
    updated_seen = set(seen)

    for item in items:
        key = item["title"] + str(item["price"])

        if key not in seen:
            new_items.append(item)
            updated_seen.add(key)

    save_seen_deals(updated_seen)

    return new_items
