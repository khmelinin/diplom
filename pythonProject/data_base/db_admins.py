# -*- coding: utf-8 -*-
import sqlite3

db = sqlite3.connect('policlinic_tg_bot.db')

# Курсор sql
c = db.cursor()

c.execute('create table if not exists admins(id integer primary key autoincrement, title nvarchar(100), password nvarchar(30))')

c.execute("insert into admins (title, password) values ('Администратор 1' , '112233')")
c.execute("insert into admins (title, password) values ('Теропевтов Т.Т.' , '111111')")

db.commit()
c.close()
db.close()