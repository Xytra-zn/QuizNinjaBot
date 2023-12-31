from pyrogram import Client, filters

@Client.on_message(filters.command(["start"]))
async def start_command(bot, message):
    user = message.from_user
    text = f"Hello {user.mention}! Welcome to Quiz Ninja Bot. 🚀\n\n"\
           "I'm here to make learning fun through interactive quizzes. "\
           "Type /quiz to get started with a quiz!"

    await message.reply_text(text)

