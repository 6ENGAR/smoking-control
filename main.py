import telebot
from config import TG_API

bot = telebot.TeleBot(TG_API, parse_mode="Markdown")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет')


if __name__ == '__main__':
    bot.infinity_polling()

