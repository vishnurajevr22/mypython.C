create database students;
use students;
create table employee(sname varchar(100),age int,address varchar(250),standard int);

insert into employee(sname,age,address,standard)values("raj",23,"cdm",15);

insert into employee(sname,age,address,standard)values("mano",23,"myl",45),("nono",67,"boo",89);
select*from employee;

select*from employee where age<40;
select sname,standard from employee where age<40;
select sname,standard from employee where  sname ="mano";

SET sql_safe_updates=0;
update employee set age=42  where sname="nono";

select min(age) from employee;
select count(sname) from employee where age=42;

alter table employee add grade int;
alter table employee drop grade;

drop table employee;
