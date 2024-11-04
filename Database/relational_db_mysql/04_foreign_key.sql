create table S(SID integer, SName varchar(10), primary key(SID));
insert into S(SID, SName) values(810342,'Bobo');

create table P(PID integer, FSID integer, primary key(PID), foreign key(FSID) references S(SID));

select* from S;
select* from P;
