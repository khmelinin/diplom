--create database policlinic1;

use policlinic1;

drop table if exists Рекомендации_справочник;
drop table if exists Пользователь_Врач;
drop table if exists Пользователь_Пациент;
drop table if exists Пользователь
drop table if exists Мероприятие;
drop table if exists Болезнь;
drop table if exists Группа_заболеваний;
drop table if exists Врач;
drop table if exists Специализация;
drop table if exists Рекомендации;
drop table if exists Пациент;
drop table if exists Услуга;
drop table if exists Справочник_услуг;

GO

create table Группа_заболеваний
(
	ID integer primary key not null identity,
	Название nvarchar(300) not null,
);

create table Болезнь
(
	ID integer primary key not null identity,
	Название nvarchar(300) not null,
	ID_Группа_Заболеваний integer references Группа_заболеваний(ID) not null,
	Хроническая bit not null default 0,
);

create table Справочник_услуг
(
	ID integer primary key not null identity,
	Название nvarchar(300) not null,
	Название_ГОСТ nvarchar(300) default NULL
);

create table Услуга
(
	ID integer primary key not null identity,
	ID_Справочник_услуг integer references Справочник_услуг(ID) not null,
	Описание nvarchar(max) not null default '-',
	Цена money not null
);

create table Пациент
(
	ID integer primary key not null identity,
	Фамилия nvarchar(300) not null,
	Имя nvarchar(300) not null,
	Отчество nvarchar(300) default NULL,
	Пол bit not null,
	Дата_рождения date not null,
	Телефон nvarchar(30) default NULL

);

create table Специализация
(
	ID integer primary key not null identity,
	Название nvarchar(300) not null
);

create table Врач
(
	ID integer primary key not null identity,
	Фамилия nvarchar(300) not null,
	Имя nvarchar(300) not null,
	Отчество nvarchar(300) default NULL,
	ID_Специализация integer references Специализация(ID) not null
);

create table Рекомендации
(
	ID integer primary key not null identity,
	ID_Пациент integer references Пациент(ID) not null,
	Текст_рекомендации nvarchar(max) not null,
	ID_Услуга integer references Услуга(ID) default NULL,
	Дата_следующего_приема date default NULL,
	ID_Рекомендации_предыдущее integer references Рекомендации(ID) default NULL
);

create table Мероприятие
(
	ID integer primary key not null identity,
	ID_Врач integer references Врач(ID) not null,
	ID_Пациент integer references Пациент(ID) not null,
	ID_Услуга integer references Услуга(ID) not null,
	ID_Рекомендации integer references Рекомендации(ID) default NULL,
	Дата_плановая date not null,
	Дата_фактическая date default NULL,
	ID_Мероприятие_предыдущее integer references Мероприятие(ID) default NULL
	--Дата_записи date not null default GETDATE()
);

create table Пользователь
(
	ID integer primary key not null identity,
	Username nvarchar(300) not null,
	Password nvarchar(300) not null,
	UserRights integer not null default 0
);

create table Пользователь_Пациент
(
	ID_Пользователь integer references Пользователь(ID) not null,
	ID_Пациент integer references Пациент(ID) not null
);

create table Пользователь_Врач
(
	ID_Пользователь integer references Пользователь(ID) not null,
	ID_Врач integer references Врач(ID) not null
);

create table Рекомендации_справочник
(
	ID integer primary key not null identity,
	ID_Услуга integer references Услуга(ID) default NULL,
	Текст_рекомендации nvarchar(max) not null
);