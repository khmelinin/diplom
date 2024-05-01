import time
import traceback

import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6594447134:AAEl5yF-IsRu6AiPKlehFZT52P3tCUtoCSI')
admin_general_password = 'Policlinic2024'
database_path = 'data_base/policlinic_tg_bot.db'

def load_all_sessions_for_admin(admin):
    sessions = []
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    #cur.execute(f"select session_title, title, phone, sign_up_date, sign_up_time, created_datetime from journal where session_title = (select session_title from sessions where expert = '{admin}')")
    cur.execute(f"select session_title, title, phone, sign_up_date, sign_up_time, created_datetime from journal where expert_id = (select id from experts where title = '{admin}')")
    s = cur.fetchall()
    for el in s:
        sessions.append(el)

    cur.close()
    conn.close()
    return sessions

def load_today_sessions_for_admin(admin):
    sessions = []
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    #cur.execute(f"select session_title, title, phone, sign_up_date, sign_up_time, created_datetime from journal where expert_id = '{admin}' and sign_up_date = date('now')")
    cur.execute(f"select session_title, title, phone, sign_up_date, sign_up_time, created_datetime from journal where expert_id = (select id from experts where title = '{admin}') and sign_up_date = date('now')")
    s = cur.fetchall()
    for el in s:
        sessions.append(el)

    cur.close()
    conn.close()
    return sessions

def print_all_sessions_for_admin(admin, message):
    sessions = load_all_sessions_for_admin(admin)
    bot.send_message(message.chat.id, 'Все записи:')
    for el in sessions:
        bot.send_message(message.chat.id, f"Сеанс: {el[0]}\nИмя пациента: {el[1]}\nТелефон клиента: {el[2]}\nДата проведения сеанса: {el[3]} {el[4]}\nДата создания записи: {el[5]}")

    #bot.reply_to(message, 'Меню:')
    bot.send_message(message.chat.id, f"Меню: ", reply_markup=admin_menu(f'{admin}'))

def print_today_sessions_for_admin(admin, message):
    sessions = load_today_sessions_for_admin(admin)
    bot.send_message(message.chat.id, 'Записи на сегодня:')
    for el in sessions:
        bot.send_message(message.chat.id, f"Сеанс: {el[0]}\nИмя пациента: {el[1]}\nТелефон клиента: {el[2]}\nВремя проведения сеанса: {el[4]}\nДата создания записи: {el[5]}")

    #bot.reply_to(message, 'Меню:')
    bot.send_message(message.chat.id, f"Меню: ", reply_markup=admin_menu(f'{admin}'))

def admin_menu(admin):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Посмотреть все записи', callback_data=f'admin_check_all_journal {admin}')
    btn2 = types.InlineKeyboardButton('Посмотреть записи на сегодня', callback_data=f'admin_check_today_journal {admin}')
    markup.row(btn1, btn2)
    return markup


def admin_individual_password(message):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(f"select title from admins where password = '{message.text}'")

    admins = cur.fetchall()

    if len(admins) < 1:
        try:
            bot.delete_message(message.chat.id, message.id)
        except:
            print("Ошибка при удалении/изменении сообщения")

        send = bot.send_message(message.chat.id, "Администратора с таким паролем нету, повторите попытку:")
        bot.register_next_step_handler(send, admin_individual_password)

    else:
        admin = admins[0][0]
        try:
            bot.delete_message(message.chat.id, message.id)
        except:
            print("Ошибка при удалении/изменении сообщения")
        bot.send_message(message.chat.id, f"Здравствуйте, {admin}")
        bot.send_message(message.chat.id, f"Меню: ", reply_markup=admin_menu(f'{admin}'))

    # if message.text == '123':
    #     bot.delete_message(message.chat.id, message.id)
    #     bot.send_message(message.chat.id, "Здравствуйте, Хмелинин А.М.", reply_markup=admin_menu('Хмелинин А.М.'))
    # elif message.text == '456':
    #     bot.delete_message(message.chat.id, message.id)
    #     bot.send_message(message.chat.id, "Здравствуйте, Усольцева О.С.", reply_markup=admin_menu('Усольцева О.С.'))
    # elif message.text == '789':
    #     bot.delete_message(message.chat.id, message.id)
    #     bot.send_message(message.chat.id, "Здравствуйте, Мартынова О.А.", reply_markup=admin_menu('Мартынова О.А.'))
    # elif message.text == '000':
    #     bot.delete_message(message.chat.id, message.id)
    #     bot.send_message(message.chat.id, "Здравствуйте, Специалист 111", reply_markup=admin_menu('Специалист 111'))
    #
    # else:
    #     bot.delete_message(message.chat.id, message.id)
    #     send = bot.send_message(message.chat.id, "Администратора с таким паролем нету, повторите попытку:")
    #     bot.register_next_step_handler(send, admin_individual_password)

    cur.close()
    conn.close()

def admin_general_login(message):
    if message.text == admin_general_password:
        try:
            bot.delete_message(message.chat.id, message.id)
        except:
            print("Ошибка при удалении/изменении сообщения")
        send = bot.send_message(message.chat.id, "Общий административный пароль принят.\nВведите индивидуальный пароль:")
        bot.register_next_step_handler(send, admin_individual_password)
    else:
        try:
            bot.delete_message(message.chat.id, message.id)
        except:
            print("Ошибка при удалении/изменении сообщения")
        bot.send_message(message.chat.id, "Общий административный пароль не верен, для повтора введите '/start'")

@bot.message_handler(commands=['start'])
def main(message):
    if message.chat.type == 'private':
        send = bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}, введите общий административный пароль:')
        bot.register_next_step_handler(send, admin_general_login)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! --->
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data.startswith('admin_check_all_journal'):
        admin = callback.data.replace('admin_check_all_journal ', '')

        try:
            bot.edit_message_text('Меню выбрано', callback.message.chat.id, callback.message.message_id, reply_markup=None)
        except:
            print("Ошибка при удалении/изменении сообщения")

        print_all_sessions_for_admin(admin, callback.message)
    elif callback.data.startswith('admin_check_today_journal'):
        admin = callback.data.replace('admin_check_today_journal ', '')

        try:
            bot.edit_message_text('Меню выбрано', callback.message.chat.id, callback.message.message_id, reply_markup=None)
        except:
            print("Ошибка при удалении/изменении сообщения")

        print_today_sessions_for_admin(admin, callback.message)




def telebot_polling1():
    try:
        bot.polling(none_stop=True)
    except:
        traceback_error_string = traceback.format_exc()
        with open("Error.Log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime(
                "%c") + "\r\n<<ERROR polling>>\r\n" + traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(10)
        telebot_polling1()

telebot_polling1()

#bot.polling(none_stop = True)