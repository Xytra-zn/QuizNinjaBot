from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority"

# Creating a connection to MongoDB
client = MongoClient(MONGODB_URL)

# Getting the 'quiz_ninja' database
db = client['quiz_ninja']

# Getting the 'stats' collection
stats = db['stats']

async def add_user(chat_id, user_id):
    user = stats.find_one({"_id": user_id})

    if user is None:
        stats.insert_one({"_id": user_id, "total_chats": 1})
    else:
        stats.update_one({"_id": user_id}, {"$inc": {"total_chats": 1}})

    chat = stats.find_one({"_id": chat_id})

    if chat is None:
        stats.insert_one({"_id": chat_id, "total_users": 1})
    else:
        stats.update_one({"_id": chat_id}, {"$inc": {"total_users": 1}})

async def get_stats():
    chat_stats = stats.find_one({"_id": 0})

    if chat_stats is None:
        chat_stats = {"total_chats": 0, "total_users": 0}
    else:
        chat_stats["total_chats"] = chat_stats.get("total_chats", 0)
        chat_stats["total_users"] = chat_stats.get("total_users", 0)

    return chat_stats

@Client.on_message(filters.command(["stats", "bot"]))
async def stats_command(bot, message):
    start_time = time.time()
    user = message.from_user
    chat_id = message.chat.id

    # Add the user to the database
    await add_user(chat_id, user.id)

    # Get the total chats and users
    total_chats, total_users = (await get_stats()).values()

    # Sending the stats message with response time
    text = f"Total chats: {total_chats}\n"\
           f"Total users: {total_users}\n"\
           f"Response time: {round((time.time() - start_time) * 1000, 2)} ms"

    await bot.send_message(chat_id, text)
