import os
import motor.motor_asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from aiogram.utils import executor
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

connection_string = "mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority"
db = AsyncIOMotorClient(connection_string).db_name
bot = Bot(token="6920434282:AAE0tBg8b8K1XRp3cWTzoqJdIG5I4imASJg", parse_mode=ParseMode.HTML)
bot.db = db

class MyBot(Bot):
    async def on_message(self, message: types.Message):
        await register_user(self.db, message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await register_chat(self.db, message.chat.id, message.chat.title)
        return await super().on_message(message)

    async def on_chat_member(self, chat_member: types.ChatMemberUpdated):
        await register_user(self.db, chat_member.new_chat_member.user.id, chat_member.new_chat_member.user.username, chat_member.new_chat_member.user.first_name, chat_member.new_chat_member.user.last_name)
        await register_chat(self.db, chat_member.chat.id, chat_member.chat.title)
        return await super().on_chat_member(chat_member)

async def register_user(db, user_id, username, first_name, last_name):
    users = db["users"]
    user = await users.find_one({"id": user_id})
    if not user:
        await users.insert_one({
            "id": user_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name
        })

async def register_chat(db, chat_id, title):
    chats = db["chats"]
    chat = await chats.find_one({"id": chat_id})
    if not chat:
        await chats.insert_one({
            "id": chat_id,
            "title": title
        })

def main():
    from aiogram.utils import executor
    executor.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    main()
