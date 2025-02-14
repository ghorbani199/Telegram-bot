import telebot
import os

TOKEN = os.getenv("7243469139:AAENZ5OtimmWk8JiIYskKt2Efx9Okt1wUHM")  # دریافت توکن از متغیر محیطی
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سلام! وقت بخیر به زودی به پیام شما پاسخ خواهیم داد با تشکر از صبوری شما🌹؟")

bot.infinity_polling()
