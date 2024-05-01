use policlinic1;

insert into Специализация (Название) 
values ('Хирург')

insert into Врач (ФИО, ID_Специализация) 
values ('Хирургов Х.Х.', 1)

insert into Кабинет (Номер, ID_Врач) 
values ('А-101', 1)

insert into Мед_карта (Пол) 
values (1)

insert into Пациент (ФИО, ID_Мед_карта, Телефон) 
values ('Пациентов П.П.', 1, '+7777777777')

insert into Пользователь(Username, Password, ID_Пациент)
values ('user111', 'password#111', 1)

insert into Услуга (Название, Цена)
values ('Консультация', 1000.00)

insert into Прием (ID_Врач, ID_Пациент, ID_Кабинет, ID_Услуга, Дата_приема) 
values (1, 1, 1, 1, '2024-04-14')

