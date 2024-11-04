create table T(Name varchar(10), DS int, Algo int);
insert into T(Name,DS,Algo) values('Bobo',100,100);
insert into T(Name,DS,Algo) values('Baubau',70,40);
insert into T(Name,DS,Algo) values('Bobo',100,100);

select sum(DS),sum(Algo),avg(DS),avg(Algo) from T;
select max(DS),max(Algo),min(DS),min(Algo) from T;
select count(DS) from T;
select DS+Algo from T where Name='Baubau';
select Name,sum(DS),sum(Algo) from T group by Name having count(DS)==2;

--group by 以...為群體合計
--having 合計後只顯示

