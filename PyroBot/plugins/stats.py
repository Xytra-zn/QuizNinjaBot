import logging
from pyrogram import Client, filters
from motor.motor_asyncio import AsyncIOMotorClient
from config import API_ID, API_HASH

# Database setup
MONGO_URL = "mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority"
MONGO_CLIENT = AsyncIOMotorClient(MONGO_URL)
MONGO_DB = MONGO_CLIENT['stats']

# Define client instance
app = Client("stats", api_id=API_ID, api_hash=API_HASH)

async def add_user(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    
    await MONGO_DB.users.insert_one({'id': user_id, 'name': user_name})

@app.on_message(filters.command("stats") & filters.chat(chat_id=config('GROUP_ID')))
async def get_stats(client, message):
    total_users = await MONGO_DB.users.count_documents({})
    total_chats = await MONGO_DB.chats.count_documents({})
    
    await message.reply_text(f"Total Users: {total_users}\nTotal Chats: {total_chats}")
