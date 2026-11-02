from telegram import ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    buttons = [
        [KeyboardButton("🔎 Поиск токенов")],
        [KeyboardButton("📊 Обзор рынка")],
        [KeyboardButton("🛡 Проверка рисков")],
        [KeyboardButton("⭐ Избранное")],
        [KeyboardButton("🐋 Анализ кошелька")],
        [KeyboardButton("⚙️ Настройки")],
    ]

    return ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True
    )