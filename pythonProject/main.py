import calendar
import datetime
import time
import traceback

import telebot
from telebot import types
import sqlite3

import libraries.telegramcalendar as telegramcalendar

bot = telebot.TeleBot('')
database_path = 'data_base/policlinic_tg_bot.db'
database2_path = 'data_base2/clinic_tg_bot.db'
admin_chatid = -1
# menu = []

class Client:

    def __int__(self):
        self.cur_month = None
        self.session_title = ''
        self.title = ''
        self.expert_id = -1
        self.phone = ''
        self.sign_up_date = ''
        self.sign_up_time = ''

    def add_sign_up_date(self, data):
        self.sign_up_date = self.sign_up_date + data

    def clear_all(self):
        self.cur_month = None
        self.session_title = ''
        self.title = ''
        self.expert_id = -1
        self.phone = ''
        self.sign_up_date = ''
        self.sign_up_time = ''

tmp = Client()
# Меню:

def main_menu_about():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('О клинике')
    markup.add('Наши специалисты')
    markup.add('⬅ Меню')
    return markup

def main_menu0():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add('Записаться на прием')
    markup.add('О нас')
    markup.add('Контакты')
    return markup

def main_menu1():
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    cur.execute('select title from spheres')
    s = cur.fetchall()
    btns = []
    for el in s:
        btns.append(types.KeyboardButton(el[0]))

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for el in btns:
        markup.add(el)

    #markup.add('Контакты')
    markup.add('⬅ Меню')

    cur.close()
    conn.close()

    return markup

def main_menu2(text):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(f"select title from complaints where complaints.sphere_id = (select id from spheres where title = '{text}')")
    s = cur.fetchall()
    btns = []
    for el in s:
        btns.append(types.KeyboardButton(el[0]))

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for el in btns:
        markup.add(el)

    #markup.add(types.KeyboardButton('Другое'))
    markup.add(types.KeyboardButton('⬅ Меню'))
    cur.close()
    conn.close()

    return markup

def main_menu3(text):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    # cur.execute(f"select title from sessions where sessions.complaint_id = (select id from complaints where title = '{text}')")
    cur.execute(f"select sessions.title from sessions inner join complaints_sessions on sessions.id = complaints_sessions.session_id inner join complaints on complaints.id = complaints_sessions.complaint_id where complaints.title = '{text}'")
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
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(f"select sessions.title, sessions.expert_id, sessions.description from sessions where sessions.title = '{text}'")
    session = cur.fetchall()[0]
    cur.close()
    conn.close()

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.add(types.KeyboardButton("Записаться на прием"))
    # markup.add(types.KeyboardButton('⬅ Меню'))

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Записаться на прием", callback_data='make_entry'))

    return session, markup


def load_sessions_times_for_date(date):
    times = []
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    cur.execute(f"select sign_up_time from journal where sign_up_date = '{date}'")
    s = cur.fetchall()
    for el in s:
        times.append(el[0])

    cur.close()
    conn.close()
    return times

def sign_up_another():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Отправить', callback_data=f'send_another'))
    return markup

def sign_up_start():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('⬅ Меню'))
    return markup

def sign_up_name():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Далее', callback_data=f'sign_up_name'))
    return markup

def sign_up_phone():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("<- Назад", callback_data='make_entry') ,types.InlineKeyboardButton('Далее', callback_data=f'sign_up_phone'))
    return markup

# def sign_up_month():
#     markup = types.InlineKeyboardMarkup()
#     date = datetime.datetime.now()
#     days_in_month = calendar.monthrange(date.year, date.month)[1]
#     i = 0
#     while i <= 11:
#         # print(date.strftime("%Y-%m"))
#         markup.add(types.InlineKeyboardButton(date.strftime("%Y-%m"), callback_data=f'sign_up_month {date.strftime("%Y-%m")}'))
#         date += datetime.timedelta(days=days_in_month)
#         i += 1
#     return markup
#
# def sign_up_day():
#     markup = types.InlineKeyboardMarkup()
#     s = tmp.sign_up_date.split('-')
#     now = datetime.date(int(s[0]), int(s[1]), 1)
#     # d = calendar.monthrange(int(date.strftime("%Y")), int(date.strftime("%m")))[1]
#     if datetime.datetime.now().strftime("%Y-%m") == now.strftime("%Y-%m"):
#         a = int(datetime.datetime.now().strftime("%d"))
#         b = calendar.monthrange(int(now.strftime("%Y")), int(now.strftime("%m")))[1]
#
#         while a <= b:
#             # print(now.strftime("%d"))
#             markup.add(types.InlineKeyboardButton(f'{a}', callback_data=f'sign_up_day {a}'))
#             now += datetime.timedelta(1)
#             a += 1
#     else:
#         a = 1
#         b = calendar.monthrange(int(now.strftime("%Y")), int(now.strftime("%m")))[1]
#
#         while a <= b:
#             markup.add(types.InlineKeyboardButton(f'{a}', callback_data=f'sign_up_day {a}'))
#             a += 1
#     return markup

def sign_up_date():
    cur = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, 1)
    tmp.cur_month = cur
    return(telegramcalendar.create_calendar(datetime.datetime.now().year, datetime.datetime.now().month))

def sign_up_time():
    dates = load_sessions_times_for_date(tmp.sign_up_date)
    markup = types.InlineKeyboardMarkup()
    a = 10
    b = 19
    if len(dates) == 0:
        while a <= b:
            markup.add(types.InlineKeyboardButton(f"{a}:00", callback_data=f'sign_up_time {a}:00'))
            a += 1
    else:
        while a <= b:
            if f"{a}:00" in dates:
                a += 1
                continue
            else:
                markup.add(types.InlineKeyboardButton(f"{a}:00", callback_data=f'sign_up_time {a}:00'))
            a += 1
    markup.add(types.InlineKeyboardButton(f"<- Назад", callback_data='sign_up_phone'))
    return markup

def sign_up_verify():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Подтвердить запись', callback_data=f'verify'))
    markup.add(types.InlineKeyboardButton('Отмена', callback_data=f'cancel'))

    return markup

def spheres():
    conn = sqlite3.connect(database_path)
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
    conn = sqlite3.connect(database_path)
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
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    cur.execute('select title from sessions')
    s = cur.fetchall()
    c = []
    for el in s:
        c.append(el[0])

    cur.close()
    conn.close()

    return c

def find_expert_by_id(expertId):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    cur.execute(f"select title from experts where experts.id = '{expertId}'")
    s = cur.fetchall()
    c = s[0]

    cur.close()
    conn.close()

    return c

def get_all_experts():
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()

    cur.execute(f"select title, specialization, description from experts")
    s = cur.fetchall()

    cur.close()
    conn.close()
    return s

@bot.message_handler(commands=['start'])
def main(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}:', reply_markup=main_menu0())

# @bot.message_handler(commands=['calendar'])
# def calendar(message):
#     cur = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, 1)
#     tmp.cur_month = cur
#     bot.send_message(message.chat.id, f'calendar', reply_markup=telegramcalendar.create_calendar(datetime.datetime.now().year, datetime.datetime.now().month))

@bot.message_handler(commands=['myid'])
def my_id(message):
    bot.send_message(message.chat.id, f'Ваш Id: {message.from_user.id}\nId чата: {message.chat.id}\nUsername: {message.from_user.username}')

@bot.message_handler(content_types=['text'])
def bot_message(message):
    #print(message.text)
    if message.chat.type == 'private':
        if message.text == '⬅ Меню':
            try:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
            except:
                print("Ошибка при удалении/изменении сообщения")

            # bot.edit_message_text('Выбрано',message.chat.id, message.message_id-1)
            bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}, выберите сферу услуг:', reply_markup=main_menu0())
            # menu.pop(len(menu) - 1)

        elif message.text == 'Записаться на прием':
            bot.send_message(message.chat.id, f'Выберите вариант услуг: ', reply_markup=main_menu1())

        elif message.text == 'О нас':
            bot.send_message(message.chat.id, f'Меню: О нас: ', reply_markup=main_menu_about())

        elif message.text == 'О поликлинике':
            bot.send_message(message.chat.id, f'• Канал: ')
        elif message.text == 'Наши специалисты':
            str = ""
            experts = get_all_experts()
            for el in experts:
                for e in el:
                    str+=e+"\n"
                bot.send_message(message.chat.id, str)
                str = ""
            #bot.send_message(message.chat.id, str)
            # bot.send_message(message.chat.id, '• Ольга Андреевна Мартынова – специалист по компьютерной диагностике Sensitiv Imago и Имедис: ВРТ (вегето-резонансная тестирование) и БРТ (биорезонансная терапия); специалист по пульсовой диагностике и хроносемантике. А также занимается подбором, установкой и коррекцией стелек ФормТотикс. Стаж работы более 10 лет.')
            # bot.send_message(message.chat.id, '• Ольга Сергеевна Усольцева – креативный директор Центра. Психолог и коуч. Специалист по пространственным технологиям, биодекодированию, психосоматической остеопатии, исцелению воспоминаниями. Стаж работы более 10 лет. Пациенты ласково называют Ольгу Сергеевну "волшебницей": сперва непонятно, что происходит на сеансе, а результат есть и еще какой! – волшебство, не иначе.')
            # bot.send_message(message.chat.id, '• Татьяна Павловна Мальцева – мастер по массажу. Владеет различными техниками: классический массаж, рефлекторно-сегментный, спортивный, детский, косметический и лифтинговый массажи лица, тайский массаж стоп. Стаж работы 2 года.')

        elif message.text == 'Контакты':
            bot.send_message(message.chat.id, f"• Связаться с админимтратором: ")
            bot.send_message(message.chat.id, f"• Телефон регистратуры: +7(777)7777777 \n\n• Наш адрес: г. Екатеринбург, ул. Поликлиников, д. 1 \n")


        elif message.text == 'Другое':
            # bot.send_message(message.chat.id, f"Дополнительные сведение узнайте от администратора: ")
            bot.send_message(message.chat.id, f"Другое:", reply_markup=sign_up_start())
            sent = bot.send_message(message.chat.id, f"Напишите что Вас волнует:")
            bot.register_next_step_handler(sent, set_another_session)

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
            tmp.session_title = ''
            bot.send_message(message.chat.id, f'{message.text}: ', reply_markup=main_menu3(message.text))

        elif message.text in sessions():
            # menu.append(message.text)
            a, m4 = main_menu4(message.text)
            #tmp.session_title = message.text
            if tmp.session_title != '':
                print(tmp.session_title)
                try:
                    bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
                except:
                    print("Ошибка при удалении/изменении сообщения")
            tmp.session_title = a[0]
            tmp.expert_id = a[1]
            expert_name = find_expert_by_id(tmp.expert_id)
            bot.send_message(message.chat.id, f'{a[0]}:\n\nСпециалист: {expert_name}\n\nОписание: {a[2]}', reply_markup=m4)



def set_another_session(message):
    if message.text == '⬅ Меню' or message.text == '/start':
        bot.send_message(message.chat.id, 'Отмена')
        tmp.clear_all()
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}, выберите сферу услуг:',reply_markup=main_menu1())

    else:
        tmp.session_title = f"От: @{message.from_user.username}\nПроблема: {message.text}"
        try:
            bot.edit_message_text('Отправить проблему на рассмотрение администратору:', message.chat.id, message.message_id - 1, reply_markup=sign_up_another())
        except:
            print("Ошибка при удалении/изменении сообщения")

    # elif (len(message.text) < 191):
    #     tmp.session_title = 'Другое: '+message.text
    #     tmp.expert = '' # Какой специалист ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
    #     try:
    #         bot.edit_message_text('Принято', message.chat.id, message.message_id - 1, reply_markup=sign_up_another())
    #     except:
    #         print("Ошибка при удалении/изменении сообщения")
    # elif (len(message.text) >= 191):
    #     try:
    #         bot.edit_message_text('Слишком много знаков', message.chat.id, message.message_id - 1, reply_markup=None)
    #     except:
    #         print("Ошибка при удалении/изменении сообщения")
    #     sent = bot.send_message(message.chat.id, f'Описание должно быть меньше 191 знака!\nПовторите попытку:')
    #     bot.register_next_step_handler(sent, set_name)

def set_name(message):
    if message.text == '⬅ Меню' or message.text == '/start':
        bot.send_message(message.chat.id, 'Отмена записи')
        tmp.clear_all()
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}, выберите сферу услуг:',reply_markup=main_menu1())
    elif (len(message.text) < 100):
        tmp.title = message.text
        try:
            bot.edit_message_text('Принято', message.chat.id, message.message_id-1, reply_markup=sign_up_name())
        except:
            print("Ошибка при удалении/изменении сообщения")
    elif (len(message.text) >= 100):
        try:
            bot.edit_message_text('Слишком много знаков', message.chat.id, message.message_id-1, reply_markup=None)
        except:
            print("Ошибка при удалении/изменении сообщения")
        sent = bot.send_message(message.chat.id, f'ФИО должно быть меньше 100 знаков!\nВведите ФИО и отправьте:')
        bot.register_next_step_handler(sent, set_name)


def set_phone(message):
    if message.text == '⬅ Меню' or message.text == '/start':
        bot.send_message(message.chat.id, 'Отмена записи')
        tmp.clear_all()
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}, выберите сферу услуг:', reply_markup=main_menu1())
    elif (len(message.text) < 30):
        tmp.phone = message.text
        try:
            bot.edit_message_text('Принято', message.chat.id, message.message_id-1, reply_markup=sign_up_phone())
        except:
            print("Ошибка при удалении/изменении сообщения")


    elif (len(message.text) >= 30):
        try:
            bot.edit_message_text('Слишком много знаков', message.chat.id, message.message_id - 1, reply_markup=None)
        except:

            print("Ошибка при удалении/изменении сообщения")

        sent = bot.send_message(message.chat.id, f'Номер телефона должен быть меньше 30 знаков!\nВведите контактный номер телефона и отправьте:')

        bot.register_next_step_handler(sent, set_phone)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):

    if callback.data == 'make_entry':
        try:
            bot.edit_message_text(f"{tmp.session_title}:", callback.message.chat.id, callback.message.message_id, reply_markup=None)
        except:
            print("Ошибка при удалении/изменении сообщения")
        bot.send_message(callback.message.chat.id, f"Регистрация на сеанс:", reply_markup=sign_up_start())
        sent = bot.send_message(callback.message.chat.id, f'Введите ФИО и отправьте:')
        bot.register_next_step_handler(sent, set_name)

    elif callback.data == 'make_entry_another':
        try:
            bot.edit_message_text(f"Другое:", callback.message.chat.id, callback.message.message_id, reply_markup=None)
        except:
            print("Ошибка при удалении/изменении сообщения")
        sent = bot.send_message(callback.message.chat.id, f'Введите кратко проблему/жалобу и отправьте:', reply_markup=sign_up_start())
        bot.register_next_step_handler(sent, set_another_session)

    elif callback.data == 'send_another':
        try:
            bot.edit_message_text(f"Другое:", callback.message.chat.id, callback.message.message_id, reply_markup=None)
        except:
            print("Ошибка при удалении/изменении сообщения")
        bot.send_message(admin_chatid, f"{tmp.session_title}")
        bot.send_message(callback.message.chat.id, "Отправлено, администратор скоро свяжеться с Вами")
        tmp.clear_all()

    elif callback.data == 'sign_up_name':
        try:
            bot.edit_message_text('Выбрано ФИО', callback.message.chat.id, callback.message.message_id, reply_markup=None)
        except:
            print("Ошибка при удалении/изменении сообщения")
        #tmp.title = callback.message.text
        send = bot.send_message(callback.message.chat.id, 'Введите контактный номер телефона и отправьте:')
        bot.register_next_step_handler(send, set_phone)

    elif callback.data == 'sign_up_phone':
        #tmp.phone = callback.message.text
        try:
            bot.edit_message_text("Выбран номер телефона", callback.message.chat.id, callback.message.message_id, reply_markup=None)
        except:
            print("Ошибка при удалении/изменении сообщения")
        #bot.send_message(callback.message.chat.id, 'Выберите месяц записи:', reply_markup=sign_up_month())
        bot.send_message(callback.message.chat.id, 'Выберите месяц и день записи:', reply_markup=sign_up_date())

    # elif callback.data.startswith('sign_up_month'): #callback.data.contains('sign_up_month'):
    #     try:
    #         bot.edit_message_text('Выбран месяц',callback.message.chat.id, callback.message.message_id)
    #     except:
    #         print("Ошибка при удалении/изменении сообщения")
    #     # tmp.sign_up_datetime = f'{datetime.date.today().year}-'+callback.data.split()[1]
    #     tmp.sign_up_date = callback.data.split()[1]
    #     bot.send_message(callback.message.chat.id, 'Выберите день записи:', reply_markup=sign_up_day())
    #
    #
    # elif callback.data.startswith('sign_up_day'): #callback.data.contains('sign_up_day'):
    #     try:
    #         bot.edit_message_text('Выбран день',callback.message.chat.id, callback.message.message_id)
    #     except:
    #         print("Ошибка при удалении/изменении сообщения")
    #     tmp.add_sign_up_date('-' + callback.data.split()[1])
    #     bot.send_message(callback.message.chat.id, 'Выберите время записи:', reply_markup=sign_up_time())

    # новый календарь
    elif callback.data == 'PREV-MONTH':
        pre = tmp.cur_month - datetime.timedelta(days=1)
        tmp.cur_month = datetime.datetime(pre.year, pre.month, 1)
        try:
            bot.edit_message_text('calendar', chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=telegramcalendar.create_calendar(int(pre.year), int(pre.month)))
        except:
            print("Ошибка при удалении/изменении сообщения PREV-MONTH")

    elif callback.data == 'NEXT-MONTH':
        pre = tmp.cur_month + datetime.timedelta(days=31)
        tmp.cur_month = datetime.datetime(pre.year, pre.month, 1)
        try:
            bot.edit_message_text('calendar', chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=telegramcalendar.create_calendar(int(pre.year), int(pre.month)))
        except:
            print("Ошибка при удалении/изменении сообщения NEXT-MONTH")

    elif callback.data.startswith('sign_up_date'):
        tmp.sign_up_date = callback.data.split()[1]
        date_now = datetime.datetime.now().strftime("%Y-%m-%d")
        if date_now <= tmp.sign_up_date:
            try:
                bot.edit_message_text(f'Выбрана дата: {tmp.sign_up_date}',callback.message.chat.id, callback.message.message_id)
            except:
                    print("Ошибка при удалении/изменении сообщения")
            bot.send_message(callback.message.chat.id, 'Выберите время записи (если кнопки выбора времени не отображаються, значит на этот день свободных записей нет):', reply_markup=sign_up_time())
        else:
            bot.send_message(callback.message.chat.id, 'Нельзя записаться на прошедшие дни, повторите попытку')

    elif callback.data.startswith('sign_up_time'): #callback.data.contains('sign_up_time'):
        try:
            bot.edit_message_text('Выбрано время',callback.message.chat.id, callback.message.message_id)
        except:
            print("Ошибка при удалении/изменении сообщения")
        tmp.sign_up_time = callback.data.split()[1]
        bot.send_message(callback.message.chat.id, f'Подтверждаете запись на {tmp.sign_up_date} {tmp.sign_up_time} на имя {tmp.title}, контактный телефон: {tmp.phone} ?', reply_markup=sign_up_verify())


    elif callback.data == 'verify': #callback.data.contains('verify'):
        try:
            bot.edit_message_text('Запись подтверждена',callback.message.chat.id, callback.message.message_id)
        except:
            print("Ошибка при удалении/изменении сообщения")

        try:
            conn = sqlite3.connect(database_path)
            cur = conn.cursor()
            # tmp_now = str(datetime.datetime.now().year)+'-'+str(datetime.datetime.now().month)+'-'+str(datetime.datetime.now().day)
            # cur.execute(f"select expert from sessions where title = '{tmp.session_title}'")
            # exp = cur.fetchall()
            # tmp.expert = exp[0][0]
            execute_string = f"insert into journal (session_title, title, expert_id, phone, sign_up_date, sign_up_time, created_datetime) values ('{tmp.session_title}', '{tmp.title}', {tmp.expert_id}, '{tmp.phone}', '{tmp.sign_up_date}', '{tmp.sign_up_time}', date('now'))"
            cur.execute(execute_string)
            message_string = f"Запись прошла успешно: \n{tmp.session_title},\n{tmp.title},\n{tmp.phone},\n{tmp.sign_up_date}"
            bot.send_message(callback.message.chat.id, message_string, reply_markup=main_menu0())
            tmp.clear_all()
            conn.commit()

            cur.close()
            conn.close()
        except Exception as inst:
            print(type(inst))  # the exception type
            print(inst.args)  # arguments stored in .args
            print(inst)
            tmp.clear_all()
            bot.send_message(callback.message.chat.id, f"Произошла ошибка записи, попробойте снова:", reply_markup=main_menu0())

    elif callback.data == 'cancel':
        try:
            bot.edit_message_text('Выбрано', callback.message.chat.id, callback.message.message_id)
        except:
            print("Ошибка при удалении/изменении сообщения")
        bot.send_message(callback.message.chat.id, f"Регистрация на сеанс отменена: \n{tmp.session_title},\n{tmp.title},\n{tmp.phone},\n{tmp.sign_up_date}", reply_markup=main_menu1())
        tmp.clear_all()

def telebot_polling1():
    try:
        #bot.polling(none_stop=True)
        bot.polling()
    except:
        traceback_error_string = traceback.format_exc()
        with open("Error.Log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime("%c") + "\r\n<<ERROR polling>>\r\n" + traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(10)
        telebot_polling1()

telebot_polling1()
#bot.polling(none_stop=True)