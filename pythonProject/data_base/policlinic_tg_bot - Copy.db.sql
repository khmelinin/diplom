--create database policlinic;
use policlinic

DROP TABLE complaints_sessions;
DROP TABLE sessions;
DROP TABLE complaints;
DROP TABLE spheres;
DROP TABLE journal;
DROP TABLE experts;
DROP TABLE admins;

CREATE TABLE spheres (
	id	integer primary key,
	title	nvarchar(50)
);

CREATE TABLE admins (
	id	integer primary key,
	title	nvarchar(100),
	password nvarchar(30)
);

CREATE TABLE experts (
	id	integer primary key,
	title	nvarchar(200),
	specialization	nvarchar(100),
	description	nvarchar(1000)
);

CREATE TABLE complaints (
	id	integer primary key,
	title	nvarchar(100),
	sphere_id	integer,
	FOREIGN KEY(sphere_id) REFERENCES spheres(id) on delete cascade
);

CREATE TABLE sessions (
	id	integer primary key,
	title	nvarchar(200),
	expert_id	integer,
	description	nvarchar(1000),
	FOREIGN KEY(expert_id) REFERENCES experts(id) on delete cascade
);

CREATE TABLE complaints_sessions (
	complaint_id integer primary key,
	session_id	integer,
	FOREIGN KEY(session_id) REFERENCES sessions(id) on delete cascade,
	FOREIGN KEY(complaint_id) REFERENCES complaints(id) on delete cascade
);

CREATE TABLE journal (
	id	integer primary key,
	session_title	nvarchar(200),
	title	nvarchar(100),
	expert_id	integer,
	phone	nvarchar(30),
	sign_up_date	text,
	sign_up_time	text,
	created_datetime	text,
	FOREIGN KEY(expert_id) REFERENCES experts(id) on delete cascade
);

INSERT INTO spheres (id,title) VALUES (1,'Запись к врачу');
INSERT INTO admins (id,title,password) VALUES (1,'Администратор 1','112233'),
 (2,'Теропевтов Т.Т.','111111');
INSERT INTO experts (id,title,specialization,description) VALUES (1,'Теропевтов Т.Т.','Терапевт','Терапевт с 2007'),
 (2,'Педиатров П.П.','Педиатр','Педиатр с 2007'),
 (3,'Офтальмологов О.О.','Офтальмолог','Офтальмолог с 2007'),
 (4,'Неврологов Н.Н.','Нефролог','Нефролог с 2007'),
 (5,'Стоматологов С.С.','Стоматолог','Стоматолог с 2007'),
 (6,'Онкологов О.О.','Онколог','Онколог с 2007'),
 (7,'Травматологенов Т.Т.','Травматолог','Травматолог с 2007');
INSERT INTO complaints (id,title,sphere_id) VALUES (1,'Терапевт',1),
 (2,'Педиатр',1),
 (3,'Офтальмолог',1),
 (4,'Невролог',1),
 (5,'Стоматолог',1),
 (6,'Онколог',1),
 (7,'Травматолог',1);
INSERT INTO sessions (id,title,expert_id,description) VALUES (1,'Прием у терапевта',1,'Базовая консультация'),
 (2,'Прием у педиатра',2,'Базовая консультация'),
 (3,'Прием у офтальмолога',3,'Базовая консультация'),
 (4,'Прием у невролога',4,'Базовая консультация'),
 (5,'Прием у терапевта',5,'Базовая консультация'),
 (6,'Прием у терапевта',6,'Базовая консультация'),
 (7,'Прием у терапевта',7,'Базовая консультация');
INSERT INTO complaints_sessions (complaint_id,session_id) VALUES (1,1),
 (2,2),
 (3,3),
 (4,4),
 (5,5),
 (6,6),
 (7,7);
INSERT INTO journal (id,session_title,title,expert_id,phone,sign_up_date,sign_up_time,created_datetime) VALUES (1,'Прием у терапевта','C1',1,'333','2024-02-29','19:00','2024-02-14'),
 (2,'Прием у терапевта','А',1,'123','2024-02-19','10:00','2024-02-18'),
 (3,'Прием у терапевта','Андрей',1,'999','2024-02-19','11:00','2024-02-18'),
 (4,'Прием у терапевта','Андрей',1,'777','2024-02-28','13:00','2024-02-18'),
 (5,'Прием у терапевта','Андрей Хмелинин',1,'+70000000000','2024-02-29','16:00','2024-02-28');

