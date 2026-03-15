import time
from src.pipelines.multi_brand_finder import find_best_deals
from src.alerts.deal_alert import send_alert


def run_agent():

    print("🤖 AI Deal Hunter Agent Started")

    while True:

        print("\nScanning marketplace...\n")

        deals = find_best_deals()

        if not deals:
            print("No good deals found.")
        else:

            for deal in deals[:3]:

                print("\n🔥 DEAL FOUND")
                print(deal)

                send_alert(deal)

        print("\nNext scan in 5 minutes...\n")

        time.sleep(300)