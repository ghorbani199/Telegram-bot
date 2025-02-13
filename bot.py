import telebot
import os

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("BOT_TOKEN")  

# اگر متغیر محیطی تنظیم نشده بود، به صورت مستقیم مقدار بده (ایمن نیست!)
if not TOKEN:
    TOKEN = "7243469139:AAGa41nvBGRv9x8lbWvoALVJNveWRMikGSE"

bot = telebot.TeleBot(TOKEN)

# پاسخ خودکار به همه پیام‌ها
@bot.message_handler(func=lambda message: True)
def reply_to_all(message):
    bot.send_message(message.chat.id, "سلام وقت بخیر، به زودی پاسخ خواهیم داد. با تشکر از صبوری شما🌹.")

# اجرای مداوم ربات و جلوگیری از کرش کردن
while True:
    try:
        bot.polling(none_stop=True, timeout=10)
    except Exception as e:
        print(f"خطا رخ داد: {e}")
