from pyrogram import Client, filters

LOG_GROUP_ID = "-1002014693954"

@Client.on_message(filters.command(["newpoll"]))
async def new_poll_command(bot, message):
    try:
        # Extract the JSON content from the message text
        json_content = message.text.split("/newpoll")[1].strip()
        
        # Convert the JSON content to a dictionary
        poll_data = eval(json_content)
        
        # Extract question, options, and correct_option_id from the dictionary
        question = poll_data.get("question", "")
        options = poll_data.get("options", [])
        correct_option_id = poll_data.get("correct_option_id", 0)
        
        # Send the question as a poll to the log group
        poll_message = await bot.send_poll(
            LOG_GROUP_ID,
            question,
            options=options,
            is_anonymous=False,
            allows_multiple_answers=False,
            type="quiz",
            correct_option_id=correct_option_id
        )
        
        # Send a confirmation message to the user
        await message.reply(f"A poll has been created and sent to the log group. Poll message ID: {poll_message.message_id}")
    
    except Exception as e:
        await message.reply(f"Failed to create a poll. Error: {str(e)}")
