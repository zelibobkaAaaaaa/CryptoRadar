import requests

API_URL = "https://api.dexscreener.com"

def get_token_market_data(token_address):
    url = f"{API_URL}/token-pairs/v1/solana/{token_address}"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    pairs = response.json()

    if not isinstance(pairs, list) or not pairs:
        return None

    pairs.sort(
        key=lambda pair: float(
            pair.get("liquidity", {}).get("usd") or 0
        ),
        reverse=True
    )

    pair = pairs[0]

    return {
        "name": pair.get("baseToken", {}).get("name"),
        "symbol": pair.get("baseToken", {}).get("symbol"),
        "price_usd": pair.get("priceUsd"),
        "volume_24h": pair.get("volume", {}).get("h24"),
        "liquidity_usd": pair.get("liquidity", {}).get("usd"),
        "market_cap": pair.get("marketCap"),
        "url": pair.get("url"),
    }