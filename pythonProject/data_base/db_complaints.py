# -*- coding: utf-8 -*-
import sqlite3

db = sqlite3.connect('policlinic_tg_bot.db')

# Курсор sql
c = db.cursor()

c.execute('create table if not exists complaints(id integer primary key autoincrement, title nvarchar(100), sphere_id integer, foreign key (sphere_id) references spheres (id) on delete cascade)')

c.execute(f"insert into complaints (id, title, sphere_id) values (1, 'Терапевт', 1)")
c.execute(f"insert into complaints (id, title, sphere_id) values (2, 'Педиатр', 1)")
c.execute(f"insert into complaints (id, title, sphere_id) values (3, 'Офтальмолог', 1)")
c.execute(f"insert into complaints (id, title, sphere_id) values (4, 'Невролог', 1)")
c.execute(f"insert into complaints (id, title, sphere_id) values (5, 'Стоматолог', 1)")
c.execute(f"insert into complaints (id, title, sphere_id) values (6, 'Онколог', 1)")
c.execute(f"insert into complaints (id, title, sphere_id) values (7, 'Травматолог', 1)")


db.commit()
c.close()
db.close()