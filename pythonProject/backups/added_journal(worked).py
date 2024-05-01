import datetime

import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6346836501:AAHEvgFS3JTkp-CB5_FTJDVvm98EX8rtirI')


# menu = []

class Client:
    def __int__(self):
        self.session_title = ''
        self.title = ''
        self.phone = ''
        self.sign_up_datetime = ''

    def add_sign_up_datetime(self, data):
        self.sign_up_datetime = self.sign_up_datetime + data


tmp = Client()


# Меню:
def main_menu1():
    conn = sqlite3.connect('data_base/aurora_tg_bot.db')
    cur = conn.cursor()

    cur.execute('select title from spheres')
    s = cur.fetchall()
    btns = []
    for el in s:
        btns.append(types.KeyboardButton(el[0]))

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for el in btns:
        markup.add(el)

    cur.close()
    conn.close()

    return markup


def main_menu2(text):
    conn = sqlite3.connect('data_base/aurora_tg_bot.db')
    cur = conn.cursor()
    cur.execute(
        f"select title from complaints where complaints.sphere_id = (select id from spheres where title = '{text}')")
    s = cur.fetchall()
    btns = []
    for el in s:
        btns.append(types.KeyboardButton(el[0]))

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for el in btns:
        markup.add(el)

    markup.add(types.KeyboardButton('⬅ Меню'))
    cur.close()
    conn.close()

    return markup


def main_menu3(text):
    conn = sqlite3.connect('data_base/aurora_tg_bot.db')
    cur = conn.cursor()
    cur.execute(
        f"select title from sessions where sessions.complaint_id = (select id from complaints where title = '{text}')")
    s = cur.fetchall()
    btns = []
    for el in s:
        btns.append(types.KeyboardButton(el[0]))

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for el in btns:
        markup.add(el)

    markup.add(types.KeyboardButton('⬅ Меню'))
    cur.close()
    conn.close()

    return markup


def main_menu4(text):
    conn = sqlite3.connect('data_base/aurora_tg_bot.db')
    cur = conn.cursor()
    cur.execute(f"select title, expert, description from sessions where sessions.title = '{text}'")

    session = cur.fetchall()[0]
    cur.close()
    conn.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Записаться на прием"))
    markup.add(types.KeyboardButton('⬅ Меню'))

    return session, markup


months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
times = ['10:00', '11:00', '12:00', '13:00', '14:00', '16:00', '17:00', '18:00']


def sign_up_name():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Далее', callback_data=f'sign_up_name'))
    return markup


def sign_up_phone():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Далее', callback_data=f'sign_up_phone'))
    return markup


def sign_up_month():
    markup = types.InlineKeyboardMarkup()
    for el in months:
        markup.add(types.InlineKeyboardButton(el, callback_data=f'sign_up_month {el}'))
    return markup


def sign_up_day():
    markup = types.InlineKeyboardMarkup()
    for el in days:
        markup.add(types.InlineKeyboardButton(el, callback_data=f'sign_up_day {el}'))
    return markup


def sign_up_time():
    markup = types.InlineKeyboardMarkup()
    for el in times:
        markup.add(types.InlineKeyboardButton(el, callback_data=f'sign_up_time {el}'))
    return markup


def sign_up_verify():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Подтвердить запись', callback_data=f'verify'))
    markup.add(types.InlineKeyboardButton('Отмена', callback_data=f'cancel'))

    return markup


def spheres():
    conn = sqlite3.connect('data_base/aurora_tg_bot.db')
    cur = conn.cursor()

    cur.execute('select title from spheres')
    s = cur.fetchall()
    c = []
    for el in s:
        c.append(el[0])

    cur.close()
    conn.close()

    return c


def complaints():
    conn = sqlite3.connect('data_base/aurora_tg_bot.db')
    cur = conn.cursor()

    cur.execute('select title from complaints')
    s = cur.fetchall()
    c = []
    for el in s:
        c.append(el[0])

    cur.close()
    conn.close()

    return c


def sessions():
    conn = sqlite3.connect('data_base/aurora_tg_bot.db')
    cur = conn.cursor()

    cur.execute('select title from sessions')
    s = cur.fetchall()
    c = []
    for el in s:
        c.append(el[0])

    cur.close()
    conn.close()

    return c


@bot.message_handler(commands=['start'])
def main(message):
    conn = sqlite3.connect('data_base/aurora_tg_bot.db')
    cur = conn.cursor()
    cur.execute('create table if not exists spheres(id integer primary key autoincrement, title nvarchar(50))')
    cur.execute(
        'create table if not exists complaints(id integer primary key autoincrement, title nvarchar(50), sphere_id integer, foreign key (sphere_id) references spheres (id) on delete cascade)')
    cur.execute(
        'create table if not exists sessions(id int auto_increment primary key, title varchar(50), expert varchar(50), description varchar(300))')
    cur.execute(
        'create table if not exists journal(id integer primary key autoincrement, session_title nvarchar(30), title nvarchar(50), phone nvarchar(30), sign_up_datetime text, created_datetime text)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}, выберите сферу услуг:',
                     reply_markup=main_menu1())


@bot.message_handler(commands=['myid'])
def my_id(message):
    bot.send_message(message.chat.id, f'Ваш Id: {message.from_user.id}\nId чата: {message.chat.id}')


@bot.message_handler(content_types=['text'])
def bot_message(message):
    # Назады
    if message.text == '⬅ Меню':
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}, выберите сферу услуг:',
                         reply_markup=main_menu1())
        # menu.pop(len(menu) - 1)

    # elif message.text == '⬅ Жалобы':
    #     bot.send_message(message.chat.id, f'{menu[len(menu)-2]}: ', reply_markup=main_menu3(menu[len(menu)-1]))
    #     menu.pop(len(menu) - 1)
    #
    # elif message.text == '⬅ Сеансы':
    #     bot.send_message(message.chat.id, f'{menu[len(menu)-2]}: ', reply_markup=main_menu4(menu[len(menu)-1]))
    #     menu.pop(len(menu) - 1)

    elif message.text in spheres():
        # menu.append(message.text)
        bot.send_message(message.chat.id, f'{message.text}: ', reply_markup=main_menu2(message.text))

    elif message.text in complaints():
        # menu.append(message.text)
        bot.send_message(message.chat.id, f'{message.text}: ', reply_markup=main_menu3(message.text))

    elif message.text in sessions():
        # menu.append(message.text)
        a, m4 = main_menu4(message.text)
        tmp.session_title = message.text
        bot.send_message(message.chat.id, f'{a[0]}:\n{a[1]}\n{a[2]}', reply_markup=m4)

    elif message.text == "Записаться на прием":
        # menu.append(message.text)
        m = sign_up_name()
        sent = bot.send_message(message.chat.id, f'Введите ФИО:', reply_markup=m)
        bot.register_next_step_handler(sent, set_name)
        # bot.send_message(message.chat.id, f'Выберите месяц записи:', reply_markup=m)
        # tmp.session_title = menu[menu.count()-1]


def set_name(message):
    tmp.title = message.text


def set_phone(message):
    tmp.phone = message.text


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'sign_up_name':
        # tmp.title = callback.message.text
        send = bot.send_message(callback.message.chat.id, 'Введите контактный номер телефона:',
                                reply_markup=sign_up_phone())
        bot.register_next_step_handler(send, set_phone)

    elif callback.data == 'sign_up_phone':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        # tmp.phone = callback.message.text
        bot.send_message(callback.message.chat.id, 'Выберите месяц записи:', reply_markup=sign_up_month())

    elif callback.data.startswith('sign_up_month'):  # callback.data.contains('sign_up_month'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        tmp.sign_up_datetime = f'{datetime.date.today().year}-' + callback.data.split()[1]
        bot.send_message(callback.message.chat.id, 'Выберите день записи:', reply_markup=sign_up_day())


    elif callback.data.startswith('sign_up_day'):  # callback.data.contains('sign_up_day'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        tmp.add_sign_up_datetime('-' + callback.data.split()[1])
        bot.send_message(callback.message.chat.id, 'Выберите время записи:', reply_markup=sign_up_time())

    elif callback.data.startswith('sign_up_time'):  # callback.data.contains('sign_up_time'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        tmp.add_sign_up_datetime(' ' + callback.data.split()[1])
        bot.send_message(callback.message.chat.id,
                         f'Подтверждаете на {tmp.sign_up_datetime} на имя {tmp.title}, контактный телефон: {tmp.phone} ?',
                         reply_markup=sign_up_verify())


    elif callback.data == 'verify':  # callback.data.contains('verify'):
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        conn = sqlite3.connect('data_base/aurora_tg_bot.db')
        cur = conn.cursor()
        tmp_now = str(datetime.datetime.now().year) + '-' + str(datetime.datetime.now().month) + '-' + str(
            datetime.datetime.now().day)
        cur.execute(
            f"insert into journal (session_title, title, phone, sign_up_datetime, created_datetime) values ('{tmp.session_title}', '{tmp.title}', '{tmp.phone}', '{tmp.sign_up_datetime}', '{tmp_now}')")
        bot.send_message(callback.message.chat.id,
                         f"Запись прошла успешно: \n{tmp.session_title},\n{tmp.title},\n{tmp.phone},\n{tmp.sign_up_datetime}",
                         reply_markup=main_menu1())

        conn.commit()

        cur.close()
        conn.close()


bot.polling(none_stop=True)