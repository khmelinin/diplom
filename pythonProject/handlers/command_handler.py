import telebot
from telebot import types
from markups import reply_keyboard_markups as rm, inline_keyboard_markup as im

def main(message, bot):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}', reply_markup=im.main_menu_auth())