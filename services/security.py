import logging

logger = logging.getLogger(__name__)


def analyze_token(token_data: dict):
    if not token_data:
        return {
            "risk": "unknown",
            "message": "Не удалось получить данные токена."
        }

    liquidity = (
        token_data.get("liquidity") or {}
    ).get("usd", 0)

    volume = (
        token_data.get("volume") or {}
    ).get("h24", 0)

    risks = []

    if liquidity < 1000:
        risks.append("Очень низкая ликвидность")

    if volume == 0:
        risks.append("Нет торгового объёма за 24 часа")

    if risks:
        return {
            "risk": "high",
            "message": "⚠️ Обнаружены риски:\n" + "\n".join(risks)
        }

    return {
        "risk": "unknown",
        "message": (
            "Автоматическая проверка не выявила "
            "указанных проблем. Это не гарантия безопасности токена."
        )
    }