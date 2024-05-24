import time
import traceback

import constants

from handlers import text_handler, callback_handler, command_handler

bot = constants.BOT
database2_path = constants.DATABASE_PATH

# menu = []
@bot.message_handler(commands=['start'])
def main(message):
    command_handler.main(message, bot)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    text_handler.bot_message(message, bot)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    callback_handler.callback_message(callback, bot)


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
