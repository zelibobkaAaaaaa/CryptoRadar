import aiosqlite
import os

DB_PATH = "crypto_radar.db"


async def init_db():
    os.makedirs("data", exist_ok=True)

    async with aiosqlite.connect("data/" + DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        await db.commit()