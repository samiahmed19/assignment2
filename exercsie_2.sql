create table contact(
c_id int,
email varchar(30),
fname varchar(30),
Iname varchar(30),
company varchar(30),
Active_flag int,opt_out int);

insert into contact values
(123,'a@a.com','kian','seth','ABC',1,1),
(133,'b@a.com','neha','seth','ABC',1,0),
(234,'c@c.com','puru','malik','CDF',0,0),
(342,'d@d.com','Sid','maan','TEG',1,0);


select * from contact where Active_flag=1;

delete from contact where opt_out=0;

delete from contact where company='ABC';

insert into contact values(658,'mili@gmail.com','mili','maan','DGH',1,1);

select distinct company from contact;

update contact set fname='niti' where fname='mili';

