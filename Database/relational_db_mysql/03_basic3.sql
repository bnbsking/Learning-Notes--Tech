Show databases
Show tables
Select name, salary+500 from customers
Select* from customers
Select distinct city from customers
Select city from customers limit 5
Select city from customers limit 3,7
[- -從4開始選7個
Select customers.city from customers
Select* from customers ordered by city, name // desc: 遞減排序
Select* from customers where ID=7
Select* from customers where ID between 3 and 7
Select* from customers where ID not in (‘LA’, ‘NY’)
Select concat(name,’,’,city) as newColumn from customers
Select upper(name), sqrt(salary) from customers
// avg, sum, min
Select* from customers where name like ‘A%’ or ‘-s’

SELECT customers.ID, customers.Name, orders.Name, orders.Amount
FROM customers, orders
WHERE customers.ID=orders.Customer_ID
ORDER BY customers.ID;

SELECT ct.ID, ct.Name, ord.Name, ord.Amount
FROM customers AS ct, orders AS ord
WHERE ct.ID=ord.Customer_ID
ORDER BY ct.ID;

SELECT column_name(s)
FROM table1 INNER JOIN table2 
ON table1.column_name=table2.column_name;

SELECT FirstName, LastName, Company FROM businessContacts
UNION ALL
SELECT FirstName, LastName, NULL FROM otherContacts;



Insert into customers values(‘bobo’, ‘ROC’, 99999)
Insert into customers(name) values(‘baubau’)

Update customers
Set name=‘bobo’, salary=‘999999’
Where ID=10

delete from customers
Where ID=9

Create table myTable(
Id int not null, name varchar(30) unique, salary (int) check salary>0, primary key(I’d)
)

Alter table customers add birth
Alter table customers drop column birth
Drop table customers
Alter table customers change name name2 varchar(30)
Rename table customers to customers2
