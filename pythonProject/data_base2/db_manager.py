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

def find_service_by_id(id):
    conn = sqlite3.connect(constants.DATABASE_PATH)
    cur = conn.cursor()
    cur.execute(f"select ID_Справочник_услуг, Название, Название_ГОСТ, Описание, Цена from Услуга join Справочник_услуг on Услуга.ID_Справочник_услуг = Справочник_услуг.ID where Услуга.ID = {id}")
    s = cur.fetchall()
    cur.close()
    conn.close()
    return s[0]

def insert_event(doctor_id, patient_id, service_id, date_plan, date_real, prev_event_id):
    conn = sqlite3.connect(constants.DATABASE_PATH)
    cur = conn.cursor()

    if prev_event_id == -1:
        prev_event_id = 'null'

    if date_real == '':
        cur.execute(f"insert into Мероприятие(ID_Врач, ID_Пациент, ID_Услуга, Дата_плановая, ID_Мероприятие_предыдущее) values ({doctor_id}, {patient_id}, {service_id}, '{date_plan}', {prev_event_id})")
        conn.commit()
    else:
        cur.execute(f"insert into Мероприятие(ID_Врач, ID_Пациент, ID_Услуга, Дата_плановая, Дата_фактическая, ID_Мероприятие_предыдущее) values ({doctor_id}, {patient_id}, {service_id}, '{date_plan}', '{date_real}', {prev_event_id})")
        conn.commit()

    cur.close()
    conn.close()

def find_event_by_id(id):
    conn = sqlite3.connect(constants.DATABASE_PATH)
    cur = conn.cursor()

    cur.execute(f"select Справочник_услуг.Название, Услуга.Описание, Врач.ФИО, Услуга.Цена, Мероприятие.Дата_плановая from Мероприятие join Услуга on Мероприятие.ID_Услуга = Услуга.ID join Справочник_услуг on Услуга.ID_Справочник_услуг = Справочник_услуг.ID join Врач on Мероприятие.ID_Врач = Врач.ID where Мероприятие.ID = {id}")
    s = cur.fetchall()

    cur.close()
    conn.close()
    return s[0]

def find_events_by_tgid(id):
    conn = sqlite3.connect(constants.DATABASE_PATH)
    cur = conn.cursor()

    str = f"select Пациент.ФИО, Справочник_услуг.Название, Услуга.Описание, Врач.ФИО, Услуга.Цена, Мероприятие.Дата_плановая from Мероприятие join Пациент on Мероприятие.ID_Пациент = Пациент.ID join Пользователь_Пациент on Пользователь_Пациент.ID_Пациент = Пациент.ID join Услуга on Мероприятие.ID_Услуга = Услуга.ID join Справочник_услуг on Услуга.ID_Справочник_услуг = Справочник_услуг.ID join Врач on Мероприятие.ID_Врач = Врач.ID join Пользователь on Пользователь.ID = Пользователь_Пациент.ID_Пользователь where Пользователь.Username = {id}"
    cur.execute(str)
    s = cur.fetchall()

    cur.close()
    conn.close()
    return s