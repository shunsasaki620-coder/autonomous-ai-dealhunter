from playwright.sync_api import sync_playwright
import re


def scan_mercari(keyword):

    results = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = f"https://jp.mercari.com/search?keyword={keyword}"
        page.goto(url)

        page.wait_for_timeout(5000)

        items = page.query_selector_all('a[href*="/item/"]')

        print("Found listings:", len(items))

        for item in items[:20]:

            text = item.text_content()

            if not text:
                continue

            price_match = re.search(r"¥[\d,]+", text)

            if not price_match:
                continue

            price = int(price_match.group().replace("¥", "").replace(",", ""))

            lines = [line.strip() for line in text.split("\n") if line.strip()]

            
            title = re.sub(r"^¥[\d,]+", "", lines[0]).strip()

            results.append({
                "title": title,
                "price": price
            })

        browser.close()

    return results