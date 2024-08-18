from telebot import types


def create_callback_functions(bot):
    return {
        'initial': lambda call: bot.send_message(call.message.chat.id, "🤔 Я предлагаю установить таймер и "
                                                                       "контролировать количество сигарет в день. \n\n"
                                                                       "⏰ Укажи промежуток который ты бы хотел "
                                                                       "установить между сигаретами",
                                                 reply_markup=timer_setup),
        'half': lambda call: bot.send_message(call.message.chat.id, "placeholder30"),
        'one': lambda call: bot.send_message(call.message.chat.id, "placeholder1"),
        'two': lambda call: bot.send_message(call.message.chat.id, "placeholder2"),
        'three': lambda call: bot.send_message(call.message.chat.id, "placeholder3"),
        'dive': lambda call: bot.send_message(call.message.chat.id, "placeholder5"),
    }


# there is no sense in this keyboard. just to test inline one. 'cpd' goes for cigarettes per day

smokes_per_day_intro = types.InlineKeyboardMarkup()
first_option = types.InlineKeyboardButton('🚬 0-10', callback_data='initial')
second_option = types.InlineKeyboardButton('🚬 10-20', callback_data='initial')
third_option = types.InlineKeyboardButton('🚬 20+', callback_data='initial')
smokes_per_day_intro.add(first_option, second_option, third_option)


# here user will set his break timer

timer_setup = types.InlineKeyboardMarkup()
half_an_hour = types.InlineKeyboardButton('🕐 30 мин.', callback_data='half')
one_hour = types.InlineKeyboardButton('🕙 1 час', callback_data='one')
two_hours = types.InlineKeyboardButton('🕥 2 часа', callback_data='two')
three_hours = types.InlineKeyboardButton('🕜 3 часа', callback_data='three')
five_hours = types.InlineKeyboardButton('🕞 5 часов', callback_data='five')
timer_setup.add(half_an_hour, one_hour, two_hours, three_hours, five_hours)