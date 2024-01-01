from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CLASS_11, CLASS_12, CLASS_11_12, OWNER_ID

# Initialize strings to store chat IDs
CLASS_11_STRING = ""
CLASS_12_STRING = ""
CLASS_11_12_STRING = ""

@Client.on_message(filters.command(["setup"]))
async def setup_command(bot, message):
    chat_id = message.chat.id

    # Check if the chat is already configured
    if chat_id in CLASS_11 or chat_id in CLASS_12 or chat_id in CLASS_11_12:
        await message.reply_text("This group is already configured.")
        return

    # Send a message with inline buttons to choose the class
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("11", callback_data="class_11")],
        [InlineKeyboardButton("12", callback_data="class_12")],
        [InlineKeyboardButton("11+12", callback_data="class_11_12")],
    ])

    await bot.send_message(chat_id, "Choose your class:", reply_markup=markup)

@Client.on_callback_query()
async def callback_handler(bot, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    # Get the chosen class from the callback data
    chosen_class = callback_query.data

    # Update the appropriate list based on the chosen class
    if chosen_class == "class_11":
        CLASS_11.append(chat_id)
    elif chosen_class == "class_12":
        CLASS_12.append(chat_id)
    elif chosen_class == "class_11_12":
        CLASS_11_12.append(chat_id)

    # Update the strings
    update_strings()

    await bot.answer_callback_query(callback_query.id, text="Group configured successfully!")

    # You can add additional logic or storage in your database here if needed

@Client.on_message(filters.command(["getchats"]))
async def getchats_command(bot, message):
    chats_text = f"CLASS 11 CHATS: {CLASS_11_STRING}\n\n" \
                 f"CLASS 12 CHATS: {CLASS_12_STRING}\n\n" \
                 f"CLASS 11+12 CHATS: {CLASS_11_12_STRING}\n\n"

    await bot.send_message(message.chat.id, chats_text)

def update_strings():
    global CLASS_11_STRING, CLASS_12_STRING, CLASS_11_12_STRING
    CLASS_11_STRING = ", ".join(map(str, CLASS_11))
    CLASS_12_STRING = ", ".join(map(str, CLASS_12))
    CLASS_11_12_STRING = ", ".join(map(str, CLASS_11_12))
