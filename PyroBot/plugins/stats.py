from pyrogram import Client, filters
from PyroBot.plugins.xytra import users, chats

@Client.on_message(filters.command(["stats"]))
async def stats_command(bot, message):
    # Retrieve and display stats
    total_chats = await chats.get_served_chats()
    total_users = await users.get_served_users()

    stats_text = f"📊 **Bot Statistics**\n\n"\
                 f"**Total Chats:** {len(total_chats)}\n"\
                 f"**Total Users:** {len(total_users)}"

    await bot.send_message(message.chat.id, stats_text)
