bot = telebot.TeleBot(...)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحبا بك في بوت القرآن 🌙")
  bot.polling()
