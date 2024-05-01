# import calendar
# import datetime
import sqlite3

database_path = 'data_base/policlinic_tg_bot.db'
text = 'Прием у терапевта'

conn = sqlite3.connect(database_path)
cur = conn.cursor()

#execute_string = "insert into journal (session_title, title, expert_id, phone, sign_up_date, sign_up_time, created_datetime) values ('Прием у терапевта', 'АМХ1', 1, '777', '2024-02-23', '17:00', date('now'))"
#cur.execute(execute_string)

cur.execute("select * from journal")
#cur.execute(f"select session_title, title, phone, sign_up_date, sign_up_time, created_datetime from journal where expert_id = (select id from experts where title = 'Теропевтов Т.Т.') and sign_up_date = date('now')")
cur.execute(f"select session_title, title, phone, sign_up_date, sign_up_time, created_datetime from journal where expert_id = (select id from experts where title = 'Теропевтов Т.Т.')")
session = cur.fetchall()
print(session)

cur.execute("select * from journal")
session = cur.fetchall()
print(session)

cur.close()
conn.close()