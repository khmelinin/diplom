import sqlite3

db = sqlite3.connect('policlinic_tg_bot.db')

# Курсор sql
c = db.cursor()

c.execute('create table if not exists experts(id integer primary key autoincrement, title nvarchar(200), specialization nvarchar(100), description nvarchar(1000))')
c.execute(f"insert into experts (id, title, specialization, description) values (1, 'Теропевтов Т.Т.', 'Терапевт', 'Терапевт с 2007')")
c.execute(f"insert into experts (id, title, specialization, description) values (2, 'Педиатров П.П.', 'Педиатр', 'Педиатр с 2007')")
c.execute(f"insert into experts (id, title, specialization, description) values (3, 'Офтальмологов О.О.', 'Офтальмолог', 'Офтальмолог с 2007')")
c.execute(f"insert into experts (id, title, specialization, description) values (4, 'Неврологов Н.Н.', 'Невролог', 'Нефролог с 2007')")
c.execute(f"insert into experts (id, title, specialization, description) values (5, 'Стоматологов С.С.', 'Стоматолог', 'Стоматолог с 2007')")
c.execute(f"insert into experts (id, title, specialization, description) values (6, 'Онкологов О.О.', 'Онколог', 'Онколог с 2007')")
c.execute(f"insert into experts (id, title, specialization, description) values (7, 'Травматологенов Т.Т.', 'Травматолог', 'Травматолог с 2007')")

c.execute("select * from experts")
print("Experts:\n", c.fetchall())

db.commit()
c.close()
db.close()