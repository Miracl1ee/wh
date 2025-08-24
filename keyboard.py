<<<<<<< HEAD
from telebot import types


def keyboard():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("CSV", callback_data='csv')
    btn2 = types.InlineKeyboardButton("XLSX", callback_data='xlsx')
    btn3 = types.InlineKeyboardButton("База данных", callback_data='db')
    btn4 = types.InlineKeyboardButton("Поиск задания", callback_data='search')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

def exit_keyboard():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Выход", callback_data='exit')
    markup.add(btn)
    return markup

def delete_keyboard():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Да ✔️', callback_data='Yes')
    btn1 = types.InlineKeyboardButton('Нет ❌', callback_data='No')
    markup.add(btn, btn1)
    return markup

=======
from telebot import types


def keyboard():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("CSV", callback_data='csv')
    btn2 = types.InlineKeyboardButton("XLSX", callback_data='xlsx')
    btn3 = types.InlineKeyboardButton("База данных", callback_data='db')
    btn4 = types.InlineKeyboardButton("Поиск задания", callback_data='search')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

def exit_keyboard():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("Выход", callback_data='exit')
    markup.add(btn)
    return markup

def delete_keyboard():
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Да ✔️', callback_data='Yes')
    btn1 = types.InlineKeyboardButton('Нет ❌', callback_data='No')
    markup.add(btn, btn1)
    return markup

>>>>>>> a9f594b995eb050cb5db63099ae58e515d2999b4
