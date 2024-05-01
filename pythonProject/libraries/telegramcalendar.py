
"""
Base methods for calendar keyboard creation and processing.
"""

from telebot import types
import datetime
import calendar


calendar_response_message = "You selected %s"


def separate_callback_data(data):
    """ Separate the callback data"""
    return data.split(";")


def create_calendar(year=None,month=None):
    """
    Create an inline keyboard with the provided year and month
    :param int year: Year to use in the calendar, if None the current year is used.
    :param int month: Month to use in the calendar, if None the current month is used.
    :return: Returns the InlineKeyboardMarkup object with the calendar.
    """
    now = datetime.datetime.now()
    if year == None: year = now.year
    if month == None: month = now.month

    #data_ignore = create_callback_data("IGNORE", year, month, 0)
    keyboard = []
    #First row - Month and Year
    row=[]
    row.append(types.InlineKeyboardButton(str(year)+'.'+str(month),callback_data='data_ignore'))
    keyboard.append(row)
    #Second row - Week Days
    row=[]
    for day in ["Пн","Вт","Ср","Чт","Пт","Сб","Вс"]:
        row.append(types.InlineKeyboardButton(day,callback_data='data_ignore'))
    keyboard.append(row)

    my_calendar = calendar.monthcalendar(year, month)
    for week in my_calendar:
        row=[]
        for day in week:
            if(day==0):
                row.append(types.InlineKeyboardButton(" ",callback_data='data_ignore'))
            else:
                #row.append(types.InlineKeyboardButton(str(day),callback_data=create_callback_data("DAY",year,month,day)))
                #row.append(types.InlineKeyboardButton(str(day), callback_data=f"sign_up_date {year}-{month}-{day}"))
                row.append(types.InlineKeyboardButton(str(day), callback_data=f"sign_up_date {datetime.date(year, month, day)}"))
        keyboard.append(row)
    #Last row - Buttons
    row=[]
    # row.append(types.InlineKeyboardButton("<",callback_data=create_callback_data("PREV-MONTH",year,month,day)))
    # row.append(types.InlineKeyboardButton(" ",callback_data=data_ignore))
    # row.append(types.InlineKeyboardButton(">",callback_data=create_callback_data("NEXT-MONTH",year,month,day)))

    row.append(types.InlineKeyboardButton("<", callback_data="PREV-MONTH"))
    row.append(types.InlineKeyboardButton("<- Назад", callback_data='sign_up_name'))
    row.append(types.InlineKeyboardButton(">", callback_data="NEXT-MONTH"))
    keyboard.append(row)

    return types.InlineKeyboardMarkup(keyboard)

