## Q1: Select Subject id, Subject Name, Subject Code, Course Duration in One Query?
```MYSQL
   SELECT Subject.sub_id, Subject.sub_name, Subject.sub_code, Course.Duration
   FROM Subject
   JOIN Course ON Subject.sub_id = Course.sub_id;
```
## Q2: Select Subject id, Subject Name, Subject Code, Course Duration, Professor First_name, Professor Last_name, in One Query?
```MYSQL
   SELECT Subject.sub_id, Subject.sub_name, Subject.sub_code, Course.Duration, Professor.F_name, Professor.L_name
   FROM Subject
   JOIN Course ON Subject.sub_id = Course.sub_id
   JOIN Professor ON Course.P_id = Professor.P_id;
```
## Q3: Select All Students With Their Address In one Query?
```MYSQL
   SELECT Student.stu_id, Student.F_name, Student.F_telephone, Student.Birth_date, Address.A_id, Address.city, Address.line1
   FROM Student
   JOIN Student_Address ON Student.stu_id = Student_Address.stu_id
   JOIN Address ON Address.A_id = Student_Address.A_id;
```
