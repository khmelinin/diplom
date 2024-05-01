# -*- coding: utf-8 -*-
import sqlite3

db = sqlite3.connect('policlinic_tg_bot.db')

# Курсор sql
c = db.cursor()

c.execute('create table if not exists spheres(id integer primary key autoincrement, title nvarchar(50))')
c.execute(f"insert into spheres (title) values ('Запись к врачу')")



# c.execute("select * from spheres")
# print("Spheres:\n", c.fetchall())
#
# c.execute("select * from complaints")
# print("Complaints")
# s = c.fetchall()
# for el in s:
#     print(el)
#
# c.execute("select * from sessions")
# print("Sessions")
# s = c.fetchall()
# for el in s:
#     print(el)
#
# c.execute("select * from complaints_sessions")
# print("Complaints_Sessions")
# s = c.fetchall()
# for el in s:
#     print(el)
#
# c.execute("select * from journal")
# print("Journal")
# s = c.fetchall()
# for el in s:
#     print(el)
#
# c.execute("select * from admins")
# print("Admins")
# s = c.fetchall()
# for el in s:
#     print(el)

# print()
# c.execute(f"select session_title, title, expert, phone, sign_up_date, created_datetime from journal where session_title = (select session_title from sessions where expert = 'Специалист 111')")
# print(c.fetchall())
#
# print('---')
# c.execute(f"select session_title, title, expert, phone, sign_up_date, created_datetime from journal where session_title = (select session_title from sessions where expert = 'Специалист 111') and sign_up_date >= date('now') and sign_up_date < date('now', '+1 day')")
# print(c.fetchall())

db.commit()
c.close()
db.close()