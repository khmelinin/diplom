from markups import reply_keyboard_markups as rm, inline_keyboard_markup as im
from models import Client, Event
from data_base2 import db_manager
import analyze_patient

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

    elif callback.data == 'registration_child':
        delete_last_message_callback(callback, bot)
        bot.send_message(callback.message.chat.id, f"Регистрация:", reply_markup=im.menu_registration())
        sent = bot.send_message(callback.message.chat.id, f'Введите ФИО и отправьте:')
        bot.register_next_step_handler(sent, rm.set_name)

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
        delete_last_message_callback(callback, bot)
        try:
            analyze_patient.analyze_first_event_by_age()
        except:
            print("Ошибка анализа")
        bot.send_message(callback.message.chat.id, f'Регистрация завершена',reply_markup=im.main_menu_auth())

    elif callback.data == 'login':
        patient = db_manager.find_patient_all_data(callback.from_user.id)[0]
        Client.tmpClient.name = patient[0]
        Client.tmpClient.sex = patient[1]
        Client.tmpClient.birthday = patient[2]
        Client.tmpClient.phone = patient[3]
        bot.send_message(callback.message.chat.id, f'Выполнен логин', reply_markup=im.main_menu_0())

    #elif callback.data == 'age':
        #age = analyze_patient.analyze_first_event_by_age()
        #bot.send_message(callback.message.chat.id, f'{age}')

    elif callback.data == 'my_events':
        event = db_manager.find_events_by_tgid(callback.from_user.id)
        for e in event:
            msg = f"Пациент: {e[0]}\nПрием: {e[1]}\nОписание: {e[2]}\nВрач: {e[3]}\nДата: {e[5]}\nЦена: {e[4]}"
            bot.send_message(callback.message.chat.id, msg, reply_markup=im.event_accept_cancel())



def delete_last_message_callback(callback, bot):
    try:
        bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    except:
        print("Ошибка при удалении сообщения")
