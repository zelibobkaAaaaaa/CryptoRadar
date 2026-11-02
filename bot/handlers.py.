from telegram import Update
from telegram.ext import (
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

from bot.keyboards import main_keyboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Добро пожаловать в Crypto Radar!\n\n"
        "Выбери нужный раздел:",
        reply_markup=main_keyboard()
    )


async def menu_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    text = update.message.text

    responses = {
        "🔎 Поиск токенов":
            "Поиск новых токенов Solana готовится.",
        "📊 Обзор рынка":
            "Здесь появится рыночная статистика.",
        "🛡 Проверка рисков":
            "Отправь команду /token и адрес токена.",
        "⭐ Избранное":
            "Раздел избранных токенов готовится.",
        "🐋 Анализ кошелька":
            "Аналитика публичных кошельков готовится.",
        "⚙️ Настройки":
            "Настройки Crypto Radar появятся здесь.",
    }

    response = responses.get(
        text,
        "Неизвестная команда. Используй меню."
    )

    await update.message.reply_text(response)


def register_handlers(application):
    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            menu_handler
        )
    )