import time
from telebot import types


def create_callback_functions(bot):
    return {
        'initial': lambda call: handle_initial(bot, call),
        '30': lambda call: handle_timer(bot, call, 30),
        '60': lambda call: handle_timer(bot, call, 60),
        '120': lambda call: handle_timer(bot, call, 120),
        '180': lambda call: handle_timer(bot, call, 180),
        '300': lambda call: handle_timer(bot, call, 300),
    }


def handle_initial(bot, call):
    bot.send_message(call.message.chat.id, "🤔 Я предлагаю установить таймер и контролировать количество сигарет в "
                                           "день. \n\n⏰ Укажи промежуток который ты бы хотел установить между"
                                           " сигаретами",reply_markup=timer_setup)


def handle_timer(bot, call, timer):
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    bot.send_message(call.message.chat.id, f"⏳ Твой таймер установлен на {timer} минут. Следи за временем 👇")
    waiter = int(timer)
    msg_for_an_edit = bot.send_message(call.message.chat.id, f"Осталось 👉 {waiter} 👈 минут")
    while waiter > 0:
        waiter -= 1
        time.sleep(60)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=msg_for_an_edit.message_id,
                              text=f"Осталось {waiter} минут")
        if waiter == 0:
            bot.send_message(call.message.chat.id, f"🔉 Время вышло")


# there is no sense in this keyboard. just to test inline one

smokes_per_day_intro = types.InlineKeyboardMarkup()
first_option = types.InlineKeyboardButton('🚬 0-10', callback_data='initial')
second_option = types.InlineKeyboardButton('🚬 10-20', callback_data='initial')
third_option = types.InlineKeyboardButton('🚬 20+', callback_data='initial')
smokes_per_day_intro.add(first_option, second_option, third_option)


# here user will set his break timer

timer_setup = types.InlineKeyboardMarkup()
half_an_hour = types.InlineKeyboardButton('🕐 30 мин.', callback_data='30')
one_hour = types.InlineKeyboardButton('🕙 1 час', callback_data='60')
two_hours = types.InlineKeyboardButton('🕥 2 часа', callback_data='120')
three_hours = types.InlineKeyboardButton('🕜 3 часа', callback_data='180')
five_hours = types.InlineKeyboardButton('🕞 5 часов', callback_data='300')
timer_setup.add(half_an_hour, one_hour, two_hours, three_hours, five_hours)