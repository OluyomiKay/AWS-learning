start transaction;
insert into university.students value(100111,"Timy Todd",80,"D");
update university.students set Name="Emily Smith" where ID = 124500;
delete from university.students where ID = 100000;
select * from university.students;
commit;