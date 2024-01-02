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

# Maximum number of retry attempts
MAX_RETRIES = 5

# Define a function to get a question from the bard api with retry mechanism
def get_question():
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            # Send a request to the bard api with the query
            response = requests.get("https://api.safone.dev/bard?message=give%20a%20random%20class%2011th%20chapter%20jee%20previous%20year%20question%20from%20any%20of%20three%20subjects%20%5Bphysic%2C%20chemistry%20and%20maths%5D%20in%20this%20format%20and%20nothing%20extra%3A-%20%7B%20%20%20%22question%22%3A%20%22What%20is%20the%20capital%20of%20France%3F%22%2C%20%20%20%22options%22%3A%20%5B%22Paris%22%2C%20%22Berlin%22%2C%20%22London%22%2C%20%22Rome%22%5D%2C%20%20%20%22correct_option_id%22%3A%200%20%7D")
            # Parse the response as json
            data = response.json()
            
            if "text" in data["candidates"][0]["content"]["parts"][0]:
                # New response format
                question = data["candidates"][0]["content"]["parts"][0]["text"]["text"]
                options = data["candidates"][0]["content"]["parts"][0]["text"]["options"]
                correct_option_id = data["candidates"][0]["content"]["parts"][0]["text"]["correct_option_id"]
            else:
                # Old response format
                question = data["candidates"][0]["content"]["parts"][0]["text"]["question"]
                options = data["candidates"][0]["content"]["parts"][0]["text"]["options"]
                correct_option_id = data["candidates"][0]["content"]["parts"][0]["text"]["correct_option_id"]

            # Return the question, options, and correct option id as a tuple
            return question, options, correct_option_id
        except Exception as e:
            print(f"Attempt {attempt} failed. Error: {e}")

    # If all attempts fail, print a failure message
    print("Failed to get response from the API after multiple attempts.")
    # Return the last API response if needed
    return None
