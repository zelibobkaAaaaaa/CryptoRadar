import aiohttp


async def get_token_info(address: str):
    url = f"https://api.dexscreener.com/latest/dex/tokens/{address}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=15) as response:
                if response.status != 200:
                    return None

                data = await response.json()
                pairs = data.get("pairs") or []

                if not pairs:
                    return None

                return pairs[0]

    except Exception as error:
        print(f"Ошибка получения данных: {error}")
        return None