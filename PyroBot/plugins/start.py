from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["start"]))
async def start_command(bot, message):
    user = message.from_user
    bot_name = "𝗤𝗨𝗜𝗭 𝗡𝗜𝗡𝗝𝗔"  # Replace with your bot's name

    # Welcome message with inline buttons
    text = f"Hᴇʏ ᴛʜᴇʀᴇ {user.first_name} ❤️\n"\
           f"☆ Mʏsᴇʟғ {bot_name}. I ᴀᴍ ᴀɴ Mᴏᴅᴇʀɴ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ʙᴀsᴇᴅ 𝚀𝚄𝙸𝚉 𝙿𝙾𝙻𝙻 𝙱𝚂ᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ sᴇɴᴅ ᴛʜᴇ ǫᴜɪᴢᴢᴇs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ ʙᴀsᴇᴅ ᴏɴ ᴘʀᴇғᴇʀᴇɴᴄᴇs !! ☆\n\n"\
           "✺ Usᴇ /help ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴍʏ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ᴜsᴇ /setup ᴛᴏ ꜱᴇᴛᴜᴘ ᴍᴇ. ✺\n\n"\
           "⊶ ᴜsᴇ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ғᴏʀ ᴍᴏʀᴇ !"

    # Inline buttons
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕𝗔𝗗𝗗 𝗠𝗘 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣", url="http://t.me/QuizNinjaBot?startgroup=true")],
            [InlineKeyboardButton("📢 CHANNEL", url="https://t.me/CODERS_ZONE"),
             InlineKeyboardButton("🆘 SUPPORT", url="https://t.me/codder_chat")],
        ]
    )

    await message.reply_text(text, reply_markup=keyboard)
