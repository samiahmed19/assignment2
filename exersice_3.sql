create table customer(
c_id int,
c_name varchar(30),
city varchar(30),
grade int,
salesman_id int);

insert into customer values
(3002,'nick','new york',100,5001),
(3007,'brad','new york',200,5001),
(3005,'graham','california',200,5002),
(300,'julian','london',300,5002),
(3004,'fabian','paris',300,5006),
(3009,'geoff','berlin',100,5003),
(3003,'jozy','moscow',200,5007),
(3001,'bead','london',null,5005);

create table salesman(
s_id int,s_name varchar(30),city varchar(30),commission float);

insert into salesman values
(5001,'james','new york',0.15),
(5002,'nail','paris',0.13),
(5005,'pit','london',0.11),
(5006,'mc lyon','paris',0.14),
(5007,'paul','rome',0.14),
(5003,'lauson','san jose',0.12);

SELECT customer.c_name, customer.city, customer.grade, salesman.s_name, salesman.city FROM
 customer INNER JOIN salesman ON customer.grade < 100 AND customer.salesman_id = salesman.s_id order by c_id ASC;