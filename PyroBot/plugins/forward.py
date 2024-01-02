from pyrogram import Client, filters
import time
import random
from config import CLASS_11_STRING

LOG_GROUP_ID = "-1002066245840"

# Initialize the last forwarded message ID
last_forwarded_message_id = None

@Client.on_message(filters.command(["startforward"]))
async def start_forward_command(bot, message):
    while True:
        try:
            # Get a random message from the database group
            random_message = await get_random_message_from_database_group(bot, LOG_GROUP_ID)

            # Forward the random message to all the class 11 chats
            await forward_message_to_class_11_chats(bot, random_message)

            # Update the last forwarded message ID
            last_forwarded_message_id = random_message.message_id

            # Wait for 15 minutes before the next forwarding
            time.sleep(900)
        except Exception as e:
            print(f"Error during forwarding: {e}")

@Client.on_message(filters.command(["forwardnow"]))
async def forward_now_command(bot, message):
    try:
        # Get the latest message from the database group
        latest_message = await get_latest_message_from_database_group(bot, LOG_GROUP_ID)

        # Forward the latest message to all the class 11 chats
        await forward_message_to_class_11_chats(bot, latest_message)

        # Update the last forwarded message ID
        last_forwarded_message_id = latest_message.message_id

        await message.reply("Manually triggered forwarding successful.")
    except Exception as e:
        await message.reply(f"Error during manual forwarding: {e}")

async def get_random_message_from_database_group(bot, chat_id):
    # Get a random message from the database group
    messages = await bot.get_chat_history(chat_id, limit=1)
    return random.choice(messages)

async def get_latest_message_from_database_group(bot, chat_id):
    # Get the latest message from the database group
    return await bot.get_messages(chat_id, 1)

async def forward_message_to_class_11_chats(bot, message):
    for chat_id in CLASS_11_STRING.split(","):
        try:
            # Forward the message to each class 11 chat
            await bot.forward_messages(chat_id.strip(), LOG_GROUP_ID, message.message_id)
        except Exception as e:
            print(f"Error during forwarding to chat {chat_id}: {e}")
