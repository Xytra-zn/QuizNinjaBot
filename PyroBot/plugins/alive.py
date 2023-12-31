from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

@Client.on_message(filters.command(["alive", "ping"]))
async def alive_command(bot, message):
    start_time = time.time()
    user = message.from_user
    chat_id = message.chat.id

    # Sending the alive message with response time
    text = f"Hᴇʟʟᴏ ᴛʜᴇʀᴇ {user.mention}!\n"\
           f"Yᴏᴜʀ ʙᴇʟᴏᴠᴇᴅ Qᴜɪᴢ NɪɴJᴀ ɪs ʜᴇʀᴇ, ᴡɪᴛʜ ʀᴇsᴘᴏɴsᴇ ᴛɪᴍᴇ ᴏғ\n"\
           f"➥ {round((time.time() - start_time) * 1000, 2)} ᴍs"

    # Inline buttons
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕ 𝗔𝗗𝗗 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣", switch_inline_query="")],
            [InlineKeyboardButton("🆘 Sᴜᴘᴘᴏʀᴛ", url="https://t.me/codder_chat")],
        ]
    )

    await bot.send_message(chat_id, text, reply_markup=keyboard)
