create database online_consultation;

create table doctors(
d_id int primary key not null,
d_name varchar(30) not null,
specialization varchar(30)
);

insert into doctors values
(101,'Dr.sami','neurosurgeon'),
(102,'Dr.ahmed','physician'),
(103,'Dr.yogi','physician'),
(104,'Dr.likitha','pediatrician'),
(105,'Dr.kiran','orthopediatrician'),
(106,'Dr.gowri','gynecologist'),
(107,'Dr.hari','dermatologist'),
(108,'Dr.madiha','oncologist'),
(109,'Dr.naveen','psychologist');

create table patient(
p_id int primary key not null,
p_name varchar(30) not null,
p_contact int);

insert into patient values
(101,'hari',98646353),
(102,'kiran',4686468),
(103,'suma',684684),
(104,'sami',3489949),
(105,'samrin',894989),
(106,'abhi',84984999),
(107,'rahul',3419884),
(108,'nida',6989849),
(109,'subha',765463);

select doctors.d_id, doctors.d_name, doctors.specialization,patient.p_name,patient.p_contact
from doctors inner join patient on doctors.d_id=patient.p_id;

create view appoinments as select doctors.d_id, doctors.d_name, doctors.specialization,patient.p_name,patient.p_contact
from doctors inner join patient on doctors.d_id=patient.p_id;

create table review(
r_id int, points_review int);

insert into review values
(101,5),
(102,3),
(103,4),
(104,2),
(105,2),
(106,3),
(107,2),
(108,2),
(109,4);
select review.r_id,doctors.d_name,review.points_review from doctors inner join review on doctors.d_id=review.r_id;
 
create view reviews as select review.r_id,doctors.d_name,review.points_review from doctors inner join review on doctors.d_id=review.r_id;

