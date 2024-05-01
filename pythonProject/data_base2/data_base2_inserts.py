import sqlite3
db = sqlite3.connect('clinic_tg_bot.db')
c = db.cursor()

# c.execute(f"insert into Группа_заболеваний (title) values ('Злокачественное новообразования')")
# c.execute(f"insert into Группа_заболеваний (title) values ('Злокачественные новообразования лимфоидной, кроветворной и родственных им тканей')")
# c.execute(f"insert into Группа_заболеваний (title) values ('Злокачественные новообразования неточно обозначенных, вторичных и неуточненных локализаций')")
#
# c.execute(f"insert into Болезнь (title, ID_Группа_Заболеваний) values ('Злокачественное новообразование губы', 1)")
# c.execute(f"insert into Болезнь (title, ID_Группа_Заболеваний) values ('Болезнь Ходжкина [лимфогранулематоз]', 2)")
# c.execute(f"insert into Болезнь (title, ID_Группа_Заболеваний) values ('Вторичное злокачественное новообразование почки и почечных лоханок', 3)")
#
# c.execute(f"insert into Справочник_услуг() values ()")



c.execute(f"insert into Группа_заболеваний (Название) values ('Группа 1')")
c.execute(f"insert into Группа_заболеваний (Название) values ('Группа 2')")
c.execute(f"insert into Группа_заболеваний (Название) values ('Группа 3')")

c.execute(f"insert into Болезнь (Название, ID_Группа_Заболеваний) values ('Болезнь 1', 1)")
c.execute(f"insert into Болезнь (Название, ID_Группа_Заболеваний, Хроническая) values ('Болезнь 2', 2, true)")
c.execute(f"insert into Болезнь (Название, ID_Группа_Заболеваний) values ('Болезнь 3', 3)")

c.execute(f"insert into Справочник_услуг(Название, Название_ГОСТ) values ('Услуга 1', 'Услуга 1 ГОСТ')")
c.execute(f"insert into Справочник_услуг(Название, Название_ГОСТ) values ('Услуга 2', 'Услуга 2 ГОСТ')")
c.execute(f"insert into Справочник_услуг(Название, Название_ГОСТ) values ('Услуга 3', 'Услуга 3 ГОСТ')")

c.execute(f"insert into Услуга(ID_Справочник_услуг, Описание, Цена) values (1, 'Описание услуги 1', 5100.00)")
c.execute(f"insert into Услуга(ID_Справочник_услуг, Описание, Цена) values (2, 'Описание услуги 2', 5200.00)")
c.execute(f"insert into Услуга(ID_Справочник_услуг, Описание, Цена) values (3, 'Описание услуги 3', 5300.00)")

c.execute(f"insert into Специализация(Название) values ('Специализация 1')")
c.execute(f"insert into Специализация(Название) values ('Специализация 2')")
c.execute(f"insert into Специализация(Название) values ('Специализация 3')")

c.execute(f"insert into Рекомендации_справочник(ID_Услуга, Текст_рекомендации) values (1, 'Текст рекомендации 1')")
c.execute(f"insert into Рекомендации_справочник(ID_Услуга, Текст_рекомендации) values (2, 'Текст рекомендации 2')")
c.execute(f"insert into Рекомендации_справочник(ID_Услуга, Текст_рекомендации) values (3, 'Текст рекомендации 3')")

c.execute(f"insert into Пользователь(Username, UserRights) values ('doc1', 1)")
c.execute(f"insert into Пользователь(Username, UserRights) values ('doc2', 1)")
c.execute(f"insert into Пользователь(Username, UserRights) values ('doc3', 1)")

c.execute(f"insert into Врач(ФИО, ID_Специализация) values ('Врач 1', 1)")
c.execute(f"insert into Врач(ФИО, ID_Специализация) values ('Врач 2', 1)")
c.execute(f"insert into Врач(ФИО, ID_Специализация) values ('Врач 3', 1)")

c.execute(f"insert into Пользователь_Врач(ID_Пользователь, ID_Врач) values (1, 1)")
c.execute(f"insert into Пользователь_Врач(ID_Пользователь, ID_Врач) values (2, 2)")
c.execute(f"insert into Пользователь_Врач(ID_Пользователь, ID_Врач) values (3, 3)")



db.commit()
c.close()
db.close()