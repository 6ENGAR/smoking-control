import telebot
import smoke_checker_db
from config import TG_API

bot = telebot.TeleBot(TG_API, parse_mode="Markdown")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    smoke_checker_db.add_new_user_to_db(message)

    bot.send_message(message.chat.id, f'Привет 👋 Я бот-помощник.\n\nЕсли тебе кажется, что ты много куришь — я тут '
                                      f'чтобы помочь тебе контролировать это 🚬')


if __name__ == '__main__':
    bot.infinity_polling()

