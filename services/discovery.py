import requests

API_URL = "https://api.dexscreener.com"

def fetch_latest_profiles():
    url = f"{API_URL}/token-profiles/latest/v1"

    response = requests.get(
        url,
        headers={"User-Agent": "CryptoRadar/1.0"},
        timeout=15
    )
    response.raise_for_status()

    data = response.json()

    if isinstance(data, dict):
        data = [data]

    return [
        {
            "address": item.get("tokenAddress"),
            "chain": item.get("chainId"),
            "url": item.get("url"),
        }
        for item in data
        if isinstance(item, dict)
        and item.get("chainId") == "solana"
        and item.get("tokenAddress")
    ]