from langchain.tools import tool
from tools.mercari_scanner import scan_mercari


@tool
def mercari_search(keyword: str) -> str:
    """
    Search Mercari for product listings.

    Input:
        keyword: item name or brand (example: patagonia, carhartt jacket)

    Returns:
        List of item titles and prices from Mercari.
    """

    results = scan_mercari(keyword)

    output = []

    for item in results:
        output.append(f"{item['title']} - ¥{item['price']}")

    return "\n".join(output)