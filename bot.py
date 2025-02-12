import telebot
import os

TOKEN = os.getenv("7379142644:AAFCX2PbOJ5dMO-RO5J99Ia_-rHNvjwRogM")  
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def reply_to_all(message):
    bot.send_message(message.chat.id, "سلام وقت بخیر، به زودی به پیام شما پاسخ خواهیم داد. با تشکر از صبوری شما.")

bot.polling()
