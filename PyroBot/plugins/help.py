from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["help"]))
async def help_command(bot, message):
    # Help message with setup instructions
    help_text = "🔧 **Setup Instructions:**\n"\
                "1. Add me to your group.\n"\
                "2. Use the `/setup` command to set up your group's preferences.\n"\
                "3. Choose class, stream, and exam focus to personalize quizzes.\n\n"\
                "✅ That's it! Your group is configured for interactive quizzes."

    # Inline buttons
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➕𝗔𝗗𝗗 𝗠𝗘 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣", url="http://t.me/QuizNinjaBot?startgroup=true")],
            [InlineKeyboardButton("📢 CHANNEL", url="https://t.me/CODERS_ZONE"),
             InlineKeyboardButton("🆘 SUPPORT", url="https://t.me/codder_chat")],
        ]
    )

    await message.reply_text(help_text, reply_markup=keyboard)
  
