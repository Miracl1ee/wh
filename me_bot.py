<<<<<<< HEAD
import telebot
from file_format import FileFormat
from database import Database
from keyboard import keyboard, exit_keyboard, delete_keyboard
from settings import TOKEN
bot = telebot.TeleBot(TOKEN)
file_Manager = FileFormat()
db = Database()
user_states = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет!😁  Выберите действие:",
        reply_markup=keyboard())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id

    if call.data == 'csv':
        user_states[chat_id] = 'waiting_for_csv'
        bot.send_message(
            chat_id,
            "Напишите строки для добавления в CSV 📃...",
            reply_markup=exit_keyboard())

    elif call.data == 'xlsx':
        user_states[chat_id] = 'waiting_for_xlsx'
        bot.send_message(
            chat_id,
            "Напишите строки для добавления в XLSX 📃...",
            reply_markup=exit_keyboard())

    elif call.data == 'db':
        bot.send_message(
            chat_id,
            "Хотите удалить <b><i>все ваши</i></b> данные из базы данных? 🗑️",
            reply_markup=delete_keyboard(), parse_mode="HTML")

    elif call.data == 'Yes':
        username = f"@{call.from_user.username}"
        db.delete_all(username)
        bot.send_message(
            chat_id,
            "Все данные <i>вашего пользователя</i> удалены из базы данных. 🗑️✔️",
            parse_mode="HTML")
        user_states[chat_id] = 'waiting_for_db'
        bot.send_message(
            chat_id,
            "Теперь вы можете добавить новые задания 📃...",
            reply_markup=exit_keyboard())

    elif call.data == 'No':
        user_states[chat_id] = 'waiting_for_db'
        bot.send_message(
            chat_id,
            "Напишите задания для добавления в Базу Данных 📃...",
            reply_markup=exit_keyboard())

    elif call.data == 'search':
        user_name = f"@{call.from_user.username}"
        user_states[chat_id] = 'waiting_for_search'
        bot.send_message(
            chat_id,
            f"Ваше имя: {user_name}\nДля поиска в Базе Данных, введите задание.📃\nЕсли хотите проверить <b><i>все задания своего пользователя</i></b>, введите « # »",
            parse_mode="HTML")

    elif call.data == 'exit':
        if chat_id in user_states:
            del user_states[chat_id]  # выход из всяких условий
        bot.send_message(
            chat_id,
            "Выход выполнен ✔️, вы можете выбрать куда записывать дальше 📃...",
            reply_markup=keyboard())


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    chat_id = message.chat.id
    if chat_id not in user_states:
        return
    if user_states[chat_id] == 'waiting_for_csv':
        file_Manager.write_to_csv(message.text)
        bot.send_message(
            chat_id,
            f"Добавлено в CSV ✔️: «{message.text}»",
            reply_markup=exit_keyboard())

    elif user_states[chat_id] == 'waiting_for_xlsx':
        file_Manager.write_to_xlsx([message.text])
        bot.send_message(
            chat_id,
            f"Добавлено в XLSX ✔️: «{message.text}»",
            reply_markup=exit_keyboard())

    elif user_states[chat_id] == 'waiting_for_db':
        username = f"@{message.from_user.username}"

        db.add_homework(username, message.text)
        bot.send_message(
            chat_id,
            f"Ваше задание: «{message.text}» добавлено ✔️",
            reply_markup=exit_keyboard())

    elif user_states[chat_id] == 'waiting_for_search':
        search = message.text.strip()
        user_name = f"@{message.from_user.username}"
        if search == "#":
            results = db.search_all(user_name)
        else:
            results = db.search_with_user_and_text(user_name, search)
        if not results:
            bot.send_message(
                chat_id,
                f"Заданий от <b>{user_name}</b> по запросу: <i>«{search}»</i> не найдено ❌",
                reply_markup=exit_keyboard(),
                parse_mode="HTML")
        else:
            bot.send_message(
                chat_id,
                f"<b>Найдено заданий от {user_name}: {len(results)} 🔍</b>",
                reply_markup = exit_keyboard(), parse_mode="HTML")
            for row in results:
                bot.send_message(
                    chat_id,
                    f"📣<b>ID:</b> {row[0]}\n👤<b>Пользователь:</b> {row[1]}\n📌<b>Задание:</b> {row[2]}", parse_mode="HTML")


if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
=======
import telebot
from file_format import FileFormat
from database import Database
from keyboard import keyboard, exit_keyboard, delete_keyboard
from settings import TOKEN
bot = telebot.TeleBot(TOKEN)
file_Manager = FileFormat()
db = Database()
user_states = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет!😁  Выберите действие:",
        reply_markup=keyboard())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id

    if call.data == 'csv':
        user_states[chat_id] = 'waiting_for_csv'
        bot.send_message(
            chat_id,
            "Напишите строки для добавления в CSV 📃...",
            reply_markup=exit_keyboard())

    elif call.data == 'xlsx':
        user_states[chat_id] = 'waiting_for_xlsx'
        bot.send_message(
            chat_id,
            "Напишите строки для добавления в XLSX 📃...",
            reply_markup=exit_keyboard())

    elif call.data == 'db':
        bot.send_message(
            chat_id,
            "Хотите удалить <b><i>все ваши</i></b> данные из базы данных? 🗑️",
            reply_markup=delete_keyboard(), parse_mode="HTML")

    elif call.data == 'Yes':
        username = f"@{call.from_user.username}"
        db.delete_all(username)
        bot.send_message(
            chat_id,
            "Все данные <i>вашего пользователя</i> удалены из базы данных. 🗑️✔️",
            parse_mode="HTML")
        user_states[chat_id] = 'waiting_for_db'
        bot.send_message(
            chat_id,
            "Теперь вы можете добавить новые задания 📃...",
            reply_markup=exit_keyboard())

    elif call.data == 'No':
        user_states[chat_id] = 'waiting_for_db'
        bot.send_message(
            chat_id,
            "Напишите задания для добавления в Базу Данных 📃...",
            reply_markup=exit_keyboard())

    elif call.data == 'search':
        user_name = f"@{call.from_user.username}"
        user_states[chat_id] = 'waiting_for_search'
        bot.send_message(
            chat_id,
            f"Ваше имя: {user_name}\nДля поиска в Базе Данных, введите задание.📃\nЕсли хотите проверить <b><i>все задания своего пользователя</i></b>, введите « # »",
            parse_mode="HTML")

    elif call.data == 'exit':
        if chat_id in user_states:
            del user_states[chat_id]  # выход из всяких условий
        bot.send_message(
            chat_id,
            "Выход выполнен ✔️, вы можете выбрать куда записывать дальше 📃...",
            reply_markup=keyboard())


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    chat_id = message.chat.id
    if chat_id not in user_states:
        return
    if user_states[chat_id] == 'waiting_for_csv':
        file_Manager.write_to_csv(message.text)
        bot.send_message(
            chat_id,
            f"Добавлено в CSV ✔️: «{message.text}»",
            reply_markup=exit_keyboard())

    elif user_states[chat_id] == 'waiting_for_xlsx':
        file_Manager.write_to_xlsx([message.text])
        bot.send_message(
            chat_id,
            f"Добавлено в XLSX ✔️: «{message.text}»",
            reply_markup=exit_keyboard())

    elif user_states[chat_id] == 'waiting_for_db':
        username = f"@{message.from_user.username}"

        db.add_homework(username, message.text)
        bot.send_message(
            chat_id,
            f"Ваше задание: «{message.text}» добавлено ✔️",
            reply_markup=exit_keyboard())

    elif user_states[chat_id] == 'waiting_for_search':
        search = message.text.strip()
        user_name = f"@{message.from_user.username}"
        if search == "#":
            results = db.search_all(user_name)
        else:
            results = db.search_with_user_and_text(user_name, search)
        if not results:
            bot.send_message(
                chat_id,
                f"Заданий от <b>{user_name}</b> по запросу: <i>«{search}»</i> не найдено ❌",
                reply_markup=exit_keyboard(),
                parse_mode="HTML")
        else:
            bot.send_message(
                chat_id,
                f"<b>Найдено заданий от {user_name}: {len(results)} 🔍</b>",
                reply_markup = exit_keyboard(), parse_mode="HTML")
            for row in results:
                bot.send_message(
                    chat_id,
                    f"📣<b>ID:</b> {row[0]}\n👤<b>Пользователь:</b> {row[1]}\n📌<b>Задание:</b> {row[2]}", parse_mode="HTML")


if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)
>>>>>>> a9f594b995eb050cb5db63099ae58e515d2999b4
