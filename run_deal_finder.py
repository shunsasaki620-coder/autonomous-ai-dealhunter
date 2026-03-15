
from src.pipelines.multi_brand_finder import find_best_deals
from src.utils.deal_alert import alert_deal

deals = find_best_deals()

for deal in deals:
    alert_deal(deal)

if __name__ == "__main__":
    deals = find_best_deals()
    for deal in deals:
        print(deal)
