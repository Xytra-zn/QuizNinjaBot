from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime, timedelta
from .setup import update_strings, CLASS_11_STRING, CLASS_12_STRING, CLASS_11_12_STRING
from config import OWNER_ID

LOGS_CHAT_ID = "-1002014693954"

# Initialize the last sent time for periodic messages
last_sent_time = datetime.now()

@Client.on_message(filters.command(["getchats"]))
async def getchats_command_owner(bot, message: Message):
    update_strings()
    class_11_chats = f"CLASS 11 CHATS: {CLASS_11_STRING}\n\n"
    class_12_chats = f"CLASS 12 CHATS: {CLASS_12_STRING}\n\n"
    class_11_12_chats = f"CLASS 11+12 CHATS: {CLASS_11_12_STRING}\n\n"

    chats_text = class_11_chats + class_12_chats + class_11_12_chats
    await bot.send_message(message.chat.id, chats_text)

@Client.on_message(filters.command(["sendchats"]) & filters.user(OWNER_ID))
async def sendchats_command_owner(bot, message: Message):
    global last_sent_time

    # Check if 12 hours have passed since the last message
    if datetime.now() - last_sent_time > timedelta(hours=12):
        update_strings()
        class_11_chats = f"CLASS 11 CHATS: {CLASS_11_STRING}\n\n"
        class_12_chats = f"CLASS 12 CHATS: {CLASS_12_STRING}\n\n"
        class_11_12_chats = f"CLASS 11+12 CHATS: {CLASS_11_12_STRING}\n\n"

        chats_text = class_11_chats + class_12_chats + class_11_12_chats
        await bot.send_message(LOGS_CHAT_ID, chats_text)

        # Update the last sent time
        last_sent_time = datetime.now()

        await bot.send_message(message.chat.id, "Chat IDs sent to logs group.")
    else:
        await bot.send_message(message.chat.id, "Chat IDs already sent in the last 12 hours.")
      
