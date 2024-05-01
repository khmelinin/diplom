import sqlite3

db = sqlite3.connect('clinic_tg_bot.db')

# Курсор sql
c = db.cursor()

c.execute("drop table if exists Рекомендации_справочник")
c.execute("drop table if exists Пользователь_Врач")
c.execute("drop table if exists Пользователь_Пациент")
c.execute("drop table if exists Пользователь")
c.execute("drop table if exists Мероприятие")
c.execute("drop table if exists Болезнь")
c.execute("drop table if exists Группа_заболеваний")
c.execute("drop table if exists Врач")
c.execute("drop table if exists Специализация")
c.execute("drop table if exists Рекомендации")
c.execute("drop table if exists Пациент")
c.execute("drop table if exists Услуга")
c.execute("drop table if exists Справочник_услуг")

c.execute('create table if not exists Группа_заболеваний('
          'ID integer primary key autoincrement, '
          'Название text not null)')

c.execute('create table if not exists Болезнь('
          'ID integer primary key autoincrement, '
          'Название text not null,'
          'ID_Группа_Заболеваний integer references Группа_заболеваний(ID) not null,'
          'Хроническая blob not null default 0)')

c.execute('create table if not exists Справочник_услуг('
          'ID integer primary key autoincrement, '
          'Название text not null,'
          'Название_ГОСТ text not null)')

c.execute("create table if not exists Услуга("
          "ID integer primary key autoincrement, "
          "ID_Справочник_услуг integer references Справочник_услуг(ID) not null,"
          "Описание text not null default '-',"
          "Цена real not null)")

c.execute("create table if not exists Пациент("
          "ID integer primary key autoincrement, "
          "ФИО text not null,"
          "Пол blob not null,"
          "Дата_рождения text not null,"
          "Телефон text default null)")

c.execute("create table if not exists Пользователь("
          "ID integer primary key autoincrement, "
          "Username text not null,"
          #"Password text not null,"
          #"ID_TG text not null,"
          "UserRights integer not null default 0)")

c.execute("create table if not exists Пользователь_Пациент("
          "ID_Пользователь integer references Пользователь(ID) not null,"
          "ID_Пациент integer references Пациент(ID) not null)")

c.execute("create table if not exists Специализация("
          "ID integer primary key autoincrement, "
          "Название text not null)")

c.execute("create table if not exists Врач("
          "ID integer primary key autoincrement, "
          "ФИО text not null,"
          "ID_Специализация integer references Специализация(ID) not null)")

c.execute("create table if not exists Пользователь_Врач("
          "ID_Пользователь integer references Пользователь(ID) not null,"
          "ID_Врач integer references Врач(ID) not null)")

c.execute("create table if not exists Рекомендации("
          "ID integer primary key autoincrement, "
          "ID_Пациент integer references Пациент(ID) not null,"
          "Текст_рекомендации text not null,"
          "ID_Услуга integer references Услуга(ID) not null,"
          "Дата_следующего_приема text default null,"
          "ID_Рекомендации_предыдущее integer references Рекомендации(ID) default null)")

c.execute("create table if not exists Рекомендации_справочник("
          "ID integer primary key autoincrement, "
          "ID_Услуга integer references Услуга(ID) not null,"
          "Текст_рекомендации text not null)")

c.execute("create table if not exists Мероприятие("
          "ID integer primary key autoincrement, "
          "ID_Врач integer references Врач(ID) not null,"
          "ID_Пациент integer references Пациент(ID) not null,"
          "ID_Услуга integer references Услуга(ID) not null,"
          "ID_Рекомендации integer references Рекомендации(ID) default null,"
          "Дата_плановая text not null,"
          "Дата_фактическая text default null,"
          "ID_Мероприятие_предыдущее integer references Мероприятие(ID) default null)")

db.commit()
c.close()
db.close()