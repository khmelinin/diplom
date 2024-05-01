import sqlite3

db = sqlite3.connect('policlinic_tg_bot.db')

# Курсор sql
c = db.cursor()

#c.execute('drop table journal')

c.execute('create table if not exists journal(id integer primary key autoincrement, session_title nvarchar(200), title nvarchar(100), expert_id integer, phone nvarchar(30), sign_up_date text, sign_up_time text, created_datetime text, foreign key (expert_id) references experts (id) on delete cascade)')


db.commit()
c.close()
db.close()