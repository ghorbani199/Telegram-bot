import telebot

TOKEN = "7243469139:AAHgHTe64Hb3yxUQaxtgFWWZTOBY3fzKUAc"  # توکن ربات

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سلام! وقت بخیر، به زودی به پیام شما پاسخ خواهیم داد. با تشکر از صبوری شما 🌹")

bot.infinity_polling()
