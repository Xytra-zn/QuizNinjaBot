from pyrogram import Client, filters
from pyrogram import enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CLASS_11, CLASS_12, CLASS_11_12, OWNER_ID

# Initialize strings to store chat IDs
CLASS_11_STRING = ""
CLASS_12_STRING = ""
CLASS_11_12_STRING = ""

@Client.on_message(filters.command(["setup"]))
async def setup_command(bot, message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Check if the user is an owner or administrator of the group
    chat_member = await bot.get_chat_member(chat_id, user_id)
    if chat_member.status in [enums.ChatMemberStatus.OWNER, enums.ChatMemberStatus.ADMINISTRATOR]:
        
        # Check if the chat is already configured
        if chat_id in CLASS_11 or chat_id in CLASS_12 or chat_id in CLASS_11_12:
            class_text = "Class: "
            if chat_id in CLASS_11:
                class_text += "11"
            elif chat_id in CLASS_12:
                class_text += "12"
            elif chat_id in CLASS_11_12:
                class_text += "11+12"
            else:
                class_text += "None selected"

            await message.reply_text(
                f"CHAT: {message.chat.title}\n{class_text}\n\n"
                "To select the preferred class for the quizzes in this chat, just click on the buttons below."
            )
            return

        # Check the condition in your database (replace 'mycol' with your actual collection name)
        if mycol.find_one({'chat_id': chat_id, 'event_id': 'on'}):
            # Send a message with inline buttons to choose the class
            markup = InlineKeyboardMarkup([
                [InlineKeyboardButton("11", callback_data="class_11")],
                [InlineKeyboardButton("12", callback_data="class_12")],
                [InlineKeyboardButton("11+12", callback_data="class_11_12")],
            ])

            await bot.send_message(chat_id, f"CHAT: {message.chat.title}\nClass: None selected\n\nTo select the preferred class for the quizzes in this chat, just click on the buttons below.", reply_markup=markup)
        else:
            await message.reply_text("The condition in the database is not met.")
    else:
        await message.reply_text("You need to be an owner or administrator to use this command.")

@Client.on_callback_query()
async def callback_handler(bot, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    # Get the chosen class from the callback data
    chosen_class = callback_query.data

    # Check if the user is an administrator of the group
    if not await bot.get_chat_member(chat_id, user_id).status in ["administrator", "creator"]:
        await bot.answer_callback_query(callback_query.id, text="You need to be an administrator to configure the group.")
        return

    # Update the appropriate list based on the chosen class
    if chosen_class == "class_11":
        remove_chat_id_from_classes(chat_id)
        CLASS_11.append(chat_id)
    elif chosen_class == "class_12":
        remove_chat_id_from_classes(chat_id)
        CLASS_12.append(chat_id)
    elif chosen_class == "class_11_12":
        remove_chat_id_from_classes(chat_id)
        CLASS_11_12.append(chat_id)

    # Update the strings
    update_strings()

    # Get the updated class text
    class_text = get_class_text(chat_id)

    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=callback_query.message.message_id,
        text=f"CHAT: {callback_query.message.chat.title}\nClass: {class_text}\n\n"
             "To select the preferred class for the quizzes in this chat, just click on the buttons below."
    )

    await bot.answer_callback_query(callback_query.id, text="Group configured successfully!")

def remove_chat_id_from_classes(chat_id):
    if chat_id in CLASS_11:
        CLASS_11.remove(chat_id)
    elif chat_id in CLASS_12:
        CLASS_12.remove(chat_id)
    elif chat_id in CLASS_11_12:
        CLASS_11_12.remove(chat_id)

def update_strings():
    global CLASS_11_STRING, CLASS_12_STRING, CLASS_11_12_STRING
    CLASS_11_STRING = ", ".join(map(str, CLASS_11))
    CLASS_12_STRING = ", ".join(map(str, CLASS_12))
    CLASS_11_12_STRING = ", ".join(map(str, CLASS_11_12))
