import telebot, whois

bot = telebot.TeleBot("bot_token")

@bot.message_handler(commands=["whois"])
def whois(message):
    domain = message.text.split()[1]
    bot.send_message(message.chat.id, whois(domain))

bot.polling()
