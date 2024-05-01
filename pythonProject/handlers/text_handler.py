import telebot
from telebot import types
import sqlite3
import constants
from markups import reply_keyboard_markups as rm, inline_keyboard_markup as im

def bot_message(message, bot):
    #print(message.text)
    if message.chat.type == 'private':
        if message.text == '⬅ Меню':
            try:
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
            except:
                print("Ошибка при удалении/изменении сообщения")

            # bot.edit_message_text('Выбрано',message.chat.id, message.message_id-1)
            bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}', reply_markup=im.main_menu_auth())
            # menu.pop(len(menu) - 1)


