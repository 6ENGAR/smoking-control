import telebot
import datetime
import keyboards
import threading
import smoke_checker_db
from config import TG_API

bot = telebot.TeleBot(TG_API, parse_mode="Markdown")

callback_functions = keyboards.create_callback_functions(bot)

time_controller = datetime.datetime.now()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        smoke_checker_db.add_new_user_to_db(message)
        smoke_checker_db.create_user_data_row(message)

        bot.send_message(message.chat.id, f'Привет 👋 Я бот-помощник.\n\nЕсли тебе кажется, что ты много куришь — я тут '
                                          f'чтобы помочь тебе контролировать это.\n\nСкаолько скуриваешь в день?',
                         reply_markup=keyboards.smokes_per_day_intro)
    except Exception as e:
        print(f'[x] Error with user {message.from_user.id}')


@bot.message_handler(func=lambda message: message.text == "😮‍💨Покурил")
def pass_def():
    pass


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data in callback_functions:
        callback_functions[call.data](call)


def start_bot():
    bot.infinity_polling()


if __name__ == '__main__':
    threading.Thread(target=start_bot).start()
    threading.Thread(target=keyboards.check_time_and_send_report, args=(bot, '251761718')).start()


