import telebot
from telebot import types

bot = telebot.TeleBot('6346836501:AAHEvgFS3JTkp-CB5_FTJDVvm98EX8rtirI')

# Меню:
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🩹 Здоровье')
    btn2 = types.KeyboardButton('💼 Работа / бизнес')
    btn3 = types.KeyboardButton('👨‍👩‍👧 Семья / взаимоотношения')
    btn4 = types.KeyboardButton('🧠 Саморазвитие')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    return markup

# Сферы:
def menu_1_health():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🍏 Жалоба / Запрос №1')
    btn2 = types.KeyboardButton('🍊 Жалоба / Запрос №2')
    back = types.KeyboardButton('⬅ Меню')
    markup.add(btn1, btn2, back)
    return markup

def menu_1_job():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🍓 Жалоба / Запрос №3')
    btn2 = types.KeyboardButton('🍇 Жалоба / Запрос №4')
    back = types.KeyboardButton('⬅ Меню')
    markup.add(btn1, btn2, back)
    return markup

def menu_1_family():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🍏 Жалоба / Запрос №1')
    btn2 = types.KeyboardButton('🍊 Жалоба / Запрос №2')
    back = types.KeyboardButton('⬅ Меню')
    markup.add(btn1, btn2, back)
    return markup

def menu_1_selfdev():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('🍓 Жалоба / Запрос №3')
    btn2 = types.KeyboardButton('🍇 Жалоба / Запрос №4')
    back = types.KeyboardButton('⬅ Меню')
    markup.add(btn1, btn2, back)
    return markup

# Жалобы:

def menu_2_1():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Процедура №1')
    btn2 = types.KeyboardButton('Процедура №2')
    back = types.KeyboardButton('⬅ Меню')
    markup.add(btn1, btn2, back)
    return markup

def menu_2_2():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Процедура №3')
    btn2 = types.KeyboardButton('Процедура №4')
    back = types.KeyboardButton('⬅ Меню')
    markup.add(btn1, btn2, back)
    return markup

def menu_2_3():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Процедура №5')
    btn2 = types.KeyboardButton('Процедура №6')
    back = types.KeyboardButton('⬅ Меню')
    markup.add(btn1, btn2, back)
    return markup

# Процедуры:

def menu_3_1():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Записаться на прием')
    back = types.KeyboardButton('⬅ Меню')
    markup.add(btn1, back)
    text = '*Процедура №1*\n\n*Специалист:*\nСпециалист №111\n*Детали сеанса:*\n...\n...\n...'
    return markup, text

def menu_3_2():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Записаться на прием')
    back = types.KeyboardButton('⬅ Меню')
    markup.add(btn1, back)
    text = '*Процедура №2*\n\n*Специалист:*\nСпециалист №222\n*Детали сеанса:*\n...\n...\n...'
    return markup, text

def menu_3_3():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Записаться на прием')
    back = types.KeyboardButton('⬅ Меню')
    markup.add(btn1, back)
    text = '*Процедура №3*\n\n*Специалист:*\nСпециалист №333\n*Детали сеанса:*\n...\n...\n...'
    return markup, text


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}, выберите сферу услуг:', reply_markup=main_menu())

@bot.message_handler(content_types=['text'])
def bot_message(message):

    # Назады
    if message.text == '⬅ Меню':
        bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}, выберите сферу услуг:', reply_markup=main_menu())

    # Меню :ll
    elif message.text == '🩹 Здоровье':
        bot.send_message(message.chat.id, '🩹 Здоровье:', reply_markup=menu_1_health())

    elif message.text == '💼 Работа / бизнес':
        bot.send_message(message.chat.id, '💼 Работа / бизнес:', reply_markup=menu_1_job())

    elif message.text == '👨‍👩‍👧 Семья / взаимоотношения':
        bot.send_message(message.chat.id, '👨‍👩‍👧 Семья / взаимоотношения:', reply_markup=menu_1_family())

    elif message.text == '🧠 Саморазвитие':
        bot.send_message(message.chat.id, '🧠 Саморазвитие:', reply_markup=menu_1_selfdev())

    # Жалобы :
    elif message.text == '🍏 Жалоба / Запрос №1':
        bot.send_message(message.chat.id, '🍏 Жалоба / Запрос №1:', reply_markup=menu_2_1())

    elif message.text == '🍊 Жалоба / Запрос №2':
        bot.send_message(message.chat.id, '🍊 Жалоба / Запрос №2:', reply_markup=menu_2_2())

    elif message.text == '🍓 Жалоба / Запрос №3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, '🍓 Жалоба / Запрос №3:', reply_markup=menu_2_3())

    elif message.text == '🍇 Жалоба / Запрос №4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, '🍇 Жалоба / Запрос №4:', reply_markup=menu_2_1())


    # ПРОЦЕДУРЫ :
    elif message.text == 'Процедура №1':
        markup, text = menu_3_1()
        bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="Markdown")

    elif message.text == 'Процедура №2':
        markup, text = menu_3_2()
        bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="Markdown")

    elif message.text == 'Процедура №3':
        markup, text = menu_3_3()
        bot.send_message(message.chat.id, text, reply_markup=markup, parse_mode="Markdown")



bot.polling(none_stop = True)