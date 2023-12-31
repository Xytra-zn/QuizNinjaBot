from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Placeholder for saving start message ID
start_message_id = None

@Client.on_message(filters.command(["start"]))
async def start_command(bot, message):
    global start_message_id
    user = message.from_user
    bot_name = "𝗤𝗨𝗜𝗭 𝗡𝗜𝗡𝗝𝗔"  # Replace with your bot's name

    # Welcome message with inline buttons
    text = f"Hᴇʏ ᴛʜᴇʀᴇ {user.first_name} ❤️\n"\
           f"☆ Mʏsᴇʟғ {bot_name}. I ᴀᴍ ᴀɴ Mᴏᴅᴇʀɴ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ʙᴀsᴇᴅ 𝚀𝚄𝙸𝚉 𝙿𝙾𝙻𝙻 𝙱𝚂ᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ sᴇɴᴅ ᴛʜᴇ ǫᴜɪᴢᴢᴇs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ ʙᴀsᴇᴅ ᴏɴ ᴘʀᴇғᴇʀᴇɴᴄᴇs !! ☆\n\n"\
           "✺ Usᴇ /help ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴍʏ ғᴇᴀᴛᴜʀᴇs ᴀɴᴅ ᴜsᴇ /setup ᴛᴏ ꜱᴇᴛᴜᴘ ᴍᴇ. ✺\n\n"\
           "⊶ ᴜsᴇ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ғᴏʀ ᴍᴏʀᴇ !"

    # Inline buttons including "Help" button
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕𝗔𝗗𝗗 𝗠𝗘 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣", url="http://t.me/QuizNinjaBot?startgroup=true")],
            [InlineKeyboardButton("HELP", callback_data="help_button")],
            [InlineKeyboardButton("📢 CHANNEL", url="https://t.me/CODERS_ZONE"),
             InlineKeyboardButton("🆘 SUPPORT", url="https://t.me/codder_chat")],
        ]
    )

    # Send the start message
    start_message = await message.reply_text(text, reply_markup=keyboard)

    # Save the message ID for deletion
    start_message_id = start_message.message_id


@Client.on_message(filters.command(["help"]))
async def help_command(bot, message):
    global start_message_id

    # Help message with setup instructions
    help_text = "🔧 **Setup Instructions:**\n"\
                "1. Add me to your group.\n"\
                "2. Use the `/config` command to set up your group's preferences.\n"\
                "3. Choose class, stream, and exam focus to personalize quizzes.\n\n"\
                "✅ That's it! Your group is configured for interactive quizzes. Use /quiz to start!"

    # Inline buttons including "Home" button
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕𝗔𝗗𝗗 𝗠𝗘 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣", url="http://t.me/QuizNinjaBot?startgroup=true")], 
            [InlineKeyboardButton("HOME", callback_data="home_button")],
            [InlineKeyboardButton("📢 CHANNEL", url="https://t.me/CODERS_ZONE"),
             InlineKeyboardButton("🆘 SUPPORT", url="https://t.me/codder_chat")],
        ]
    )

    # Send the help message
    help_message = await message.reply_text(help_text, reply_markup=keyboard)

    # Delete the previous start message
    await bot.delete_messages(chat_id=message.chat.id, message_ids=start_message_id)

    # Save the message ID for deletion
    start_message_id = None


@Client.on_callback_query(filters.callback_query("help_button"))
async def help_button_callback(bot, query):
    # Trigger the help_command and delete the current start message
    await help_command(bot, query.message)


@Client.on_callback_query(filters.callback_query("home_button"))
async def home_button_callback(bot, query):
    # Trigger the start_command and delete the current help message
    await start_command(bot, query.message)
