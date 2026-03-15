from src.ai.resale_evaluator import estimate_resale
from src.ai.deal_reasoner import evaluate_deal


def analyze_deals(listings):

    analyzed = []

    for item in listings:

        title = item["title"]
        price = item["price"]

        try:

            resale = estimate_resale(title, price)

            profit = resale - price

            if profit <= 0:
                continue

            score = profit / resale

            reasoning = evaluate_deal(
                title,
                price,
                resale
            )

            deal = {
                "title": title,
                "price": price,
                "resale": resale,
                "profit": profit,
                "score": score,
                "reason": reasoning["reason"],
                "confidence": reasoning["confidence"]
            }

            # FILTER GOOD DEALS
            if profit > 5000 and reasoning["confidence"] > 0.7:
                analyzed.append(deal)

        except Exception as e:

            print("Error analyzing:", title)
            print(e)

    analyzed.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return analyzed