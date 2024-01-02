from pyrogram import Client, filters
import requests

LOG_GROUP_ID = "-1002014693954"

# Define a handler for the /generate_poll command
@Client.on_message(filters.command(["generate_poll"]))
async def generate_poll_command(bot, message):
    # Get a question from the bard api
    question, options, correct_option_id = get_question()

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
    await message.reply(f"A poll has been generated and sent to the log group. Poll message ID: {poll_message.message_id}")

def get_question():
    response = requests.get("https://api.safone.dev/bard?message=give%20a%20random%20class%20eleventh%20chapters%20jee%20previous%20year%20question%20in%20this%20format%20and%20nothing%20extra:-%20question%20=%20%22What%27s%20the%20best%20programming%20language?[year=2022]%22options%20=%20[%20%20%20%20%22Python%22,%20%20%20%20%22Java%22,%20%20%20%20%22JavaScript%22,%20%20%20%20%22C++%22]correct_option_id%20=%200")
    data = response.json()
    question = data["message"]
    options = data["candidates"][0]["content"]["parts"][0]["text"]["options"]
    correct_option_id = data["candidates"][0]["content"]["parts"][0]["text"]["correct_option_id"]
    return question, options, correct_option_id


