--create database policlinic1;

use policlinic1;

drop table if exists ������������_����������;
drop table if exists ������������_����;
drop table if exists ������������_�������;
drop table if exists ������������
drop table if exists �����������;
drop table if exists �������;
drop table if exists ������_�����������;
drop table if exists ����;
drop table if exists �������������;
drop table if exists ������������;
drop table if exists �������;
drop table if exists ������;
drop table if exists ����������_�����;

GO

create table ������_�����������
(
	ID integer primary key not null identity,
	�������� nvarchar(300) not null,
);

create table �������
(
	ID integer primary key not null identity,
	�������� nvarchar(300) not null,
	ID_������_����������� integer references ������_�����������(ID) not null,
	����������� bit not null default 0,
);

create table ����������_�����
(
	ID integer primary key not null identity,
	�������� nvarchar(300) not null,
	��������_���� nvarchar(300) default NULL
);

create table ������
(
	ID integer primary key not null identity,
	ID_����������_����� integer references ����������_�����(ID) not null,
	�������� nvarchar(max) not null default '-',
	���� money not null
);

create table �������
(
	ID integer primary key not null identity,
	������� nvarchar(300) not null,
	��� nvarchar(300) not null,
	�������� nvarchar(300) default NULL,
	��� bit not null,
	����_�������� date not null,
	������� nvarchar(30) default NULL

);

create table �������������
(
	ID integer primary key not null identity,
	�������� nvarchar(300) not null
);

create table ����
(
	ID integer primary key not null identity,
	������� nvarchar(300) not null,
	��� nvarchar(300) not null,
	�������� nvarchar(300) default NULL,
	ID_������������� integer references �������������(ID) not null
);

create table ������������
(
	ID integer primary key not null identity,
	ID_������� integer references �������(ID) not null,
	�����_������������ nvarchar(max) not null,
	ID_������ integer references ������(ID) default NULL,
	����_����������_������ date default NULL,
	ID_������������_���������� integer references ������������(ID) default NULL
);

create table �����������
(
	ID integer primary key not null identity,
	ID_���� integer references ����(ID) not null,
	ID_������� integer references �������(ID) not null,
	ID_������ integer references ������(ID) not null,
	ID_������������ integer references ������������(ID) default NULL,
	����_�������� date not null,
	����_����������� date default NULL,
	ID_�����������_���������� integer references �����������(ID) default NULL
	--����_������ date not null default GETDATE()
);

create table ������������
(
	ID integer primary key not null identity,
	Username nvarchar(300) not null,
	Password nvarchar(300) not null,
	UserRights integer not null default 0
);

create table ������������_�������
(
	ID_������������ integer references ������������(ID) not null,
	ID_������� integer references �������(ID) not null
);

create table ������������_����
(
	ID_������������ integer references ������������(ID) not null,
	ID_���� integer references ����(ID) not null
);

create table ������������_����������
(
	ID integer primary key not null identity,
	ID_������ integer references ������(ID) default NULL,
	�����_������������ nvarchar(max) not null
);