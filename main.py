import logging

from telegram.ext import Application
from config import BOT_TOKEN
from database import init_db
from bot.handlers import register_handlers


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


async def post_init(application):
    await init_db()
    print("База данных подключена!")


def main():
    if not BOT_TOKEN:
        raise RuntimeError("Не указан BOT_TOKEN")

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    register_handlers(app)

    print("Crypto Radar запускается...")
    app.run_polling()


if __name__ == "__main__":
    main()