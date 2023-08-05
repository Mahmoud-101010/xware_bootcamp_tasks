
## TABLE student 
```MYSQL
    CREATE TABLE student (
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(20) NOT NULL,
    age INT NOT NULL
    );
```
```MYSQL
INSERT INTO student (id, name, age) VALUES
                    (1, 'Hady', 26),
                    (2, 'Eslam', 26),
                    (3, 'Mohammed', 26),
                    (4, 'Sadiq', 26);
```


## TABLE course
```MYSQL 
    CREATE TABLE course (
    id INT PRIMARY KEY NOT NULL,
    name VARCHAR(20) NOT NULL
    );
```
```MYSQL
INSERT INTO course (id, name) VALUES
                   (1, 'A'),
                   (2, 'B'),
                   (3, 'C'),
                   (4, 'D');
```

## TABLE enrolment
```MYSQL
    CREATE TABLE enrolment (
    id INT PRIMARY KEY NOT NULL,
    student_id INT NOT NULL,
    course_id INT NOT NULL
    );
```

```MYSQL
INSERT INTO enrolment (id, student_id, course_id) VALUES
                      (1, 1, 1),
                      (2, 1, 2),
                      (3, 2, 1),
                      (4, 3, 1);
```
# Student Table
| Column   | Data Type | Constraints           |
|----------|----------|-----------------------|
| id       | int      | Primary Key, Not Null |
| name     | varchar(20) | Not Null            |
| age      | int      | Not Null             |

# Course Table
| Column   | Data Type | Constraints           |
|----------|----------|-----------------------|
| id       | int      | Primary Key, Not Null |
| name     | varchar(20) | Not Null            |

# Enrolment Table
| Column   | Data Type | Constraints                             |
|----------|----------|-----------------------------------------|
| id       | int      | Primary Key, Not Null                   |
| student_id | int    | Not Null, Foreign Key (References student.id) |
| course_id  | int    | Not Null, Foreign Key (References course.id) |

# Tasks

## 1- Select All Students enrolled in Course B
## 2- Select All Students enrolled in Course D
## 3- Select All Courses has student "Hady" in them.
## 4- Select All Courses has student "Sadiq" in them.






