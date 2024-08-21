import telebot
import keyboards
import smoke_checker_db
from config import TG_API

bot = telebot.TeleBot(TG_API, parse_mode="Markdown")

callback_functions = keyboards.create_callback_functions(bot)


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


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data in callback_functions:
        callback_functions[call.data](call)


if __name__ == '__main__':
    print(smoke_checker_db.get_timer_value('251761718'))
    bot.infinity_polling()
