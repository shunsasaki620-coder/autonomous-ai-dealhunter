def send_alert(deal):

    title = deal["title"]
    price = deal["price"]
    resale = deal["resale"]
    profit = deal["profit"]

    print("\n======================")
    print("🚨 DEAL ALERT")
    print("======================")
    print("Item:", title)
    print("Price:", price)
    print("Resale:", resale)
    print("Profit:", profit)
    print("======================\n")