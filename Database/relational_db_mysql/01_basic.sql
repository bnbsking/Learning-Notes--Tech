create table T(ID integer, Name varchar(10), primary key(ID));
alter table T add Gender char(1);
insert into T(ID, Name, Gender) values(810342,'Bobo','B');
insert into T(ID, Name, Gender) values(123456,'BauBau','B');
insert into T(ID, Name, Gender) values(654321,'Ma','G');
select distinct ID, Name from T where( (ID>0 or ID<999999) and Gender=='B') order by ID desc;

update T set Gender=='M' where Gender=='B';
delete from T where Gender=='G';
select* from T;

-- create view ... as select ... from .. where 
-- drop T -- delete T
-- alter table T drop Gender;
-- alter table T change Name NameX varchar(10);
