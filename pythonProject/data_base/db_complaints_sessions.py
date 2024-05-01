# -*- coding: utf-8 -*-
import sqlite3

db = sqlite3.connect('policlinic_tg_bot.db')

# Курсор sql
c = db.cursor()

# c.execute("drop table complaints_sessions")

c.execute("create table if not exists complaints_sessions(complaint_id integer, session_id integer, foreign key (complaint_id) references complaints (id) on delete cascade, foreign key (session_id) references sessions (id) on delete cascade)")

c.execute(f"insert into complaints_sessions (complaint_id, session_id) values (1, 1)")
c.execute(f"insert into complaints_sessions (complaint_id, session_id) values (2, 2)")
c.execute(f"insert into complaints_sessions (complaint_id, session_id) values (3, 3)")
c.execute(f"insert into complaints_sessions (complaint_id, session_id) values (4, 4)")
c.execute(f"insert into complaints_sessions (complaint_id, session_id) values (5, 5)")
c.execute(f"insert into complaints_sessions (complaint_id, session_id) values (6, 6)")
c.execute(f"insert into complaints_sessions (complaint_id, session_id) values (7, 7)")

db.commit()
c.close()
db.close()