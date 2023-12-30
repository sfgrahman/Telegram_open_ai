from config import *
import telebot
import openai
from openai import OpenAI


bot = telebot.TeleBot(BOT_API)
client = OpenAI(api_key=OPENAI_API_KEY)

chatStr =''
def ChatModal(prompt):
    global chatStr
    chatStr += f"ChatBot: {prompt}\nJarvis:"
   
    response = client.completions.create(
                    model ="gpt-3.5-turbo-instruct",
                    prompt=chatStr
                )
    print(response.choices[0].text)
    chatStr +=f"{response.choices[0].text}"
   
    return response.choices[0].text
                               
                               
@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.reply_to(message, "Hi, Welcome to ChatBot Bot tutorial")

@bot.message_handler()
def chat(message):
    try:
        reply = ChatModal(message.text)
        bot.reply_to(message, reply)
    except Exception as e:
        print(e)
        bot.reply_to(message, e)

print("Bot Started........")
bot.polling()