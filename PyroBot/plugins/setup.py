from pyrogram import Client, filters
from pyrogram import enums
import time
import random
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
    
    # Check if the user is an administrator of the group
    chat_member = await bot.get_chat_member(chat_id, user_id)
    if chat_member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
        await bot.answer_callback_query(callback_query.id, text="You need to be an administrator to configure the group.")
        return

    # Send a message with inline buttons to choose the class
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("11", callback_data="class_11")],
        [InlineKeyboardButton("12", callback_data="class_12")],
        [InlineKeyboardButton("11+12", callback_data="class_11_12")],
    ])

    class_text = get_class_text(chat_id)
    message_sent = await bot.send_message(chat_id, f"CHAT: {message.chat.title}\nClass: {class_text}\n\nTo select the preferred class for the quizzes in this chat, just click on the buttons below.", reply_markup=markup)

@Client.on_callback_query()
async def callback_handler(bot, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id
    message_id = callback_query.message.id
  

    # Check if the user is an administrator of the group
    chat_member = await bot.get_chat_member(chat_id, user_id)
    if chat_member.status not in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]:
        await bot.answer_callback_query(callback_query.id, text="You need to be an administrator to configure the group.")
        return

    # Get the chosen class from the callback data
    chosen_class = callback_query.data

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

    # Delete the original message with the buttons
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"Your class is successfully configured! ✓✓\n\nClass: {class_text}\n\nIf you want to change class, then use /setup again.")


    await bot.answer_callback_query(callback_query.id, text="Group configured successfully!")


def get_class_text(chat_id):
    if chat_id in CLASS_11:
        return "11"
    elif chat_id in CLASS_12:
        return "12"
    elif chat_id in CLASS_11_12:
        return "11+12"
    else:
        return "None selected"

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


@Client.on_message(filters.command(["allchats"]))
async def all_chats_handler(bot, message):
    chat_id = message.chat.id

    all_chats_text = f"CLASS 11 CHATS: {CLASS_11_STRING}\n\n" \
                     f"CLASS 12 CHATS: {CLASS_12_STRING}\n\n" \
                     f"CLASS 11+12 CHATS: {CLASS_11_12_STRING}\n\n"

    await bot.send_message(chat_id, all_chats_text)



# Store the message IDs of the sent messages
sent_message_ids = set()

# Store the message IDs along with their respective timestamps
sent_message_timestamps = {}

start_sending = False

@Client.on_message(filters.command('startsending') & filters.private)
async def start_sending_command(client, message):
    global start_sending
    start_sending = True
    await message.reply_text('Started sending messages...')

async def get_random_message(group_id):
    try:
        messages = []
        async for message in app.iter_history(group_id):
            if message.text and message.message_id not in sent_message_ids:
                messages.append(message)
        
        if messages:
            random_message = random.choice(messages)
            sent_message_ids.add(random_message.message_id)
            sent_message_timestamps[random_message.message_id] = time.time()
            return random_message.text
        
    except Exception as e:
        print(f"Error in get_random_message: {e}")
        return None
        
async def send_to_all_groups():
    global start_sending
    while not start_sending:
        await asyncio.sleep(1)
    
    try:
        group_ids = CLASS_11_STRING
        group_ids = list(map(int, group_ids))

        for group_id in group_ids:
            try:
                random_message = await get_random_message(int(group_id))
                
                if random_message:
                    await app.send_message(int(group_id), random_message)
            except Exception as e:
                print(f"Error sending message to group {group_id}: {e}")
                    
    except Exception as e:
        print(f"Error in send_to_all_groups: {e}")
        
    # Remove expired message IDs from the set
    current_time = time.time()
    expired_message_ids = [message_id for message_id, timestamp in sent_message_timestamps.items() if current_time - timestamp > 86400] # 86400 seconds = 24 hours
    for message_id in expired_message_ids:
        sent_message_ids.remove(message_id)
        del sent_message_timestamps[message_id]

    await asyncio.sleep(60)
    await send_to_all_groups()

