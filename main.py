import telebot
from config import TG_API
from smoke_checker_db import cursor, connection

bot = telebot.TeleBot(TG_API, parse_mode="Markdown")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    cursor.execute(f"INSERT INTO users(user_tg_id, username) VALUES ('{message.from_user.id}', "
                   f"'{message.from_user.username}');")
    connection.commit()
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} @{message.from_user.username}')


if __name__ == '__main__':
    bot.infinity_polling()

