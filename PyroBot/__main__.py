import os
import logging
import pyrogram
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_URL, OWNER_ID

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

while threading.active_count() > 1:
    time.sleep(5)
mythread.start()

if __name__ == "__main__":
    print("Starting Bot...")
    plugins = dict(root="PyroBot/plugins")
    app = pyrogram.Client(
        "BotzHub",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
