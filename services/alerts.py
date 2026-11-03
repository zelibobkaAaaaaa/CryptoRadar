import logging

logger = logging.getLogger(__name__)


async def send_alert(bot, chat_id: int, message: str):
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=message
        )
        return True

    except Exception as error:
        logger.error("Ошибка отправки уведомления: %s", error)
        return False