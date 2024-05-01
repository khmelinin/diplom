import telebot
from telebot import types
import sqlite3
import time
from models import Client
import constants
from markups import inline_keyboard_markup as im

bot = constants.BOT

def set_name(message):
    if (len(message.text) < 300):
        Client.tmpClient.name =  message.text
        bot.send_message(message.chat.id, f'Принято', reply_markup=im.next('set_phone'))
        #sent = bot.send_message(message.chat.id, f'Введите Ваш номер телефона:')
        #bot.register_next_step_handler(sent, set_phone)
    else:
        bot.send_message(message.chat.id, f'ФИО должно быть меньше 300 знаков!\nВведите ФИО и отправьте:', reply_markup=im.next('set_name'))

def set_phone(message):
    if (len(message.text) < 50):
        Client.tmpClient.phone =  message.text
        bot.send_message(message.chat.id, f'Принято', reply_markup=im.next('set_birthday'))
        #sent = bot.send_message(message.chat.id, f'Введите дату Вашего рождения в формате (год-месяц-день):\nПример: 1999-23-03')
        #bot.register_next_step_handler(sent, set_birthday)
    else:
        bot.send_message(message.chat.id, f'Номер телефона должен быть меньше 50 знаков!\nВведите номер телефона и отправьте:', reply_markup=im.next('set_phone'))

def set_birthday(message):
    try:
        if (len(message.text) == 10 and time.strptime(message.text, "%Y-%m-%d")):
            Client.tmpClient.birthday =  message.text
            bot.send_message(message.chat.id, f'Принято', reply_markup=im.next('set_sex'))
            #sent = bot.send_message(message.chat.id, f'Введите дату Вашего рождения в формате (год-месяц-день):\nПример: 1999-23-03')
            #bot.register_next_step_handler(sent, set_sex)
        else:
            bot.send_message(message.chat.id, f'Некорректно введена дата, повторите:', reply_markup=im.next('set_birthday'))
    except:
        bot.send_message(message.chat.id, f'Некорректно введена дата, повторите:', reply_markup=im.next('set_birthday'))

