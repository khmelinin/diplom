import telebot
from telebot import types
import sqlite3
import constants

def find_user_id(tg_id):
    conn = sqlite3.connect(constants.DATABASE_PATH)
    cur = conn.cursor()
    cur.execute(f"select ID from Пользователь where Username = '{tg_id}'")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s

def find_patient_id(name, birthday):
    conn = sqlite3.connect(constants.DATABASE_PATH)
    cur = conn.cursor()
    cur.execute(f"select ID from Пациент where ФИО = '{name}' and Дата_рождения = '{birthday}'")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s

def find_patient_all_data(tg_id):
    conn = sqlite3.connect(constants.DATABASE_PATH)
    cur = conn.cursor()
    cur.execute(f"select ФИО, Пол, Дата_рождения, Телефон from Пациент inner join Пользователь_Пациент on Пациент.ID = Пользователь_Пациент.ID_Пациент inner join Пользователь on Пользователь.ID = Пользователь_Пациент.ID_Пользователь where Пользователь.Username = '{tg_id}'")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s

def insert_user_patient(tg_id, name, sex, birthday, phone):
    conn = sqlite3.connect(constants.DATABASE_PATH)
    cur = conn.cursor()
    tmp_sex = 1
    if sex == 'Ж':
        tmp_sex = 0

    cur.execute(f"insert into Пользователь(Username, UserRights) values ('{tg_id}', 0)")
    cur.execute(f"insert into Пациент(ФИО, Пол, Дата_рождения, Телефон) values ('{name}', '{tmp_sex}', '{birthday}', '{phone}')")

    conn.commit()

    fui = find_user_id(tg_id)[0][0]
    fpi = find_patient_id(name, birthday)[0][0]

    cur.execute(f"insert into Пользователь_Пациент(ID_Пользователь, ID_Пациент) values ({fui}, {fpi})")

    conn.commit()

    cur.close()
    conn.close()
