import aiohttp


async def get_wallet_balance(address: str):
    url = "https://api.mainnet-beta.solana.com"

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [address]
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url,
                json=payload,
                timeout=15
            ) as response:

                if response.status != 200:
                    return None

                data = await response.json()

                if "error" in data:
                    return None

                lamports = data["result"]["value"]

                return lamports / 1_000_000_000

    except Exception:
        return None