import telebot
from telebot import types
from markups import reply_keyboard_markups as rm, inline_keyboard_markup as im
from models import Client
import db_manager

def callback_message(callback, bot):
    if callback.data == 'menu':
        delete_last_message_callback(callback, bot)
        bot.send_message(callback.message.chat.id, f'Меню',reply_markup=im.main_menu_auth())

    elif callback.data == 'registration_name':
        if(len(db_manager.find_user_id(callback.from_user.id))==0):
            delete_last_message_callback(callback, bot)
            bot.send_message(callback.message.chat.id, f"Регистрация:", reply_markup=im.menu_registration())
            sent = bot.send_message(callback.message.chat.id, f'Введите ФИО и отправьте:')
            bot.register_next_step_handler(sent, rm.set_name)
        else:
            bot.send_message(callback.message.chat.id, f"Вы уже зарегестрированы")

    elif callback.data.startswith('next'):
        tmp_data = callback.data.split()[1]
        if tmp_data == 'set_name':
            delete_last_message_callback(callback, bot)
            sent = bot.send_message(callback.message.chat.id, f'Введите ФИО и отправьте:')
            bot.register_next_step_handler(sent, rm.set_name)
        elif tmp_data == 'set_phone':
            delete_last_message_callback(callback, bot)
            sent = bot.send_message(callback.message.chat.id, f'Введите номер телефона:')
            bot.register_next_step_handler(sent, rm.set_phone)
        elif tmp_data == 'set_birthday':
            delete_last_message_callback(callback, bot)
            sent = bot.send_message(callback.message.chat.id, f'Введите дату Вашего рождения в формате (год-месяц-день):\nПример: 1999-23-03:')
            bot.register_next_step_handler(sent, rm.set_birthday)
        elif tmp_data == 'set_sex':
            delete_last_message_callback(callback, bot)
            bot.send_message(callback.message.chat.id, f'Введите пол:', reply_markup=im.set_sex())

    elif callback.data.startswith('registration_end'):
        tmp_data = callback.data.split()[1]
        Client.tmpClient.sex = tmp_data
        Client.tmpClient.tg_id = callback.from_user.id
        db_manager.insert_user_patient(Client.tmpClient.tg_id, Client.tmpClient.name, Client.tmpClient.sex, Client.tmpClient.birthday, Client.tmpClient.phone)
        bot.send_message(callback.message.chat.id, f'Регистрация завершена',reply_markup=im.main_menu_auth())

    elif callback.data == 'login':
        patient = db_manager.find_patient_all_data(callback.from_user.id)[0]
        Client.tmpClient.name = patient[0]
        Client.tmpClient.sex = patient[1]
        Client.tmpClient.birthday = patient[2]
        Client.tmpClient.phone = patient[3]



def delete_last_message_callback(callback, bot):
    try:
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    except:
        print("Ошибка при удалении сообщения: '", callback.message,"'")
