import telebot
from telebot import types
import sqlite3
from markups import inline_keyboard_markup as im

def main_menu_auth():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Зарегестрироваться', callback_data=f'registration_name'))
    markup.add(types.InlineKeyboardButton('Логин', callback_data=f'login'))
    return markup

def menu_registration():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('⬅ Меню', callback_data=f'menu'))
    return markup

def next(step):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Далее', callback_data=f'next '+step))
    return markup

def set_sex():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('М', callback_data=f'registration_end ' + 'М'))
    markup.add(types.InlineKeyboardButton('Ж', callback_data=f'registration_end ' + 'Ж'))
    return markup

