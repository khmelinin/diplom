# -*- coding: utf-8 -*-
import sqlite3

db = sqlite3.connect('policlinic_tg_bot.db')

# Курсор sql
c = db.cursor()

c.execute('create table if not exists sessions(id integer primary key autoincrement, title nvarchar(200), expert_id integer, description nvarchar(1000), foreign key (expert_id) references experts (id) on delete cascade)')

c.execute(f"insert into sessions (id, title, expert_id, description) values (1, 'Прием у терапевта', 1, 'Базовая консультация')")
c.execute(f"insert into sessions (id, title, expert_id, description) values (2, 'Прием у педиатра', 2, 'Базовая консультация')")
c.execute(f"insert into sessions (id, title, expert_id, description) values (3, 'Прием у офтальмолога', 3, 'Базовая консультация')")
c.execute(f"insert into sessions (id, title, expert_id, description) values (4, 'Прием у невролога', 4, 'Базовая консультация')")
c.execute(f"insert into sessions (id, title, expert_id, description) values (5, 'Прием у терапевта', 5, 'Базовая консультация')")
c.execute(f"insert into sessions (id, title, expert_id, description) values (6, 'Прием у терапевта', 6, 'Базовая консультация')")
c.execute(f"insert into sessions (id, title, expert_id, description) values (7, 'Прием у терапевта', 7, 'Базовая консультация')")

db.commit()
c.close()
db.close()