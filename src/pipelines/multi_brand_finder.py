from src.tools.mercari_scanner import scan_mercari
from src.pipelines.deal_analyzer import analyze_deals


def find_best_deals():

    brands = [
        "patagonia",
        "carhartt",
        "arc'teryx",
        "north face",
        "nike acg"
    ]

    all_deals = []

    for brand in brands:

        print("Scanning:", brand)

        items = scan_mercari(brand)

        deals = analyze_deals(items)

        all_deals.extend(deals)

    all_deals.sort(key=lambda x: x["profit"], reverse=True)

    return all_deals[:10]