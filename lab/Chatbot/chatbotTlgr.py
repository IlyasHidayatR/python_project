import os
import openai
import telebot

# Set your OpenAI API key from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up your Telegram Bot API token from .env file
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_API_TOKEN"))

# Define the chatbot function
def chatbot_openai(message):
    # Define the prompt
    prompt = f"""The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: {message}
AI:"""

    # Generate the completion
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )

    # Get the reply from the chatbot
    reply = response.choices[0].text

    return reply

# Define the function that handles the received messages
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    # Get the chat id
    chat_id = message.chat.id

    # Get the message from the user
    user_message = message.text

    # Call the chatbot function
    bot_reply = chatbot_openai(user_message)

    # Send the reply to the user
    bot.send_message(chat_id, bot_reply)

# Run the Telegram bot
if __name__ == "__main__":
    bot.polling()
