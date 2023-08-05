## Faculty Table
| Column Name | Data Type  | Constraints      |
|-------------|------------|------------------|
| F_id        | BIGINT     | PRIMARY KEY      |
| F_name      | VARCHAR    | NOT NULL         |

## Department Table
| Column Name | Data Type  | Constraints                        |
|-------------|------------|------------------------------------|
| D_id        | BIGINT     | PRIMARY KEY                        |
| D_name      | VARCHAR    | NOT NULL                           |
| F_id        | BIGINT     | NOT NULL, FOREIGN KEY (faculty.F_id)|

## Address Table
| Column Name | Data Type  | Constraints  |
|-------------|------------|--------------|
| A_id        | BIGINT     | PRIMARY KEY  |
| Gvernorate  | VARCHAR    | NOT NULL     |
| city        | VARCHAR(15)| NOT NULL     |
| line1       | VARCHAR    | NOT NULL     |
| line2       | VARCHAR    |              |

## Student_Address Table
| Column Name | Data Type  | Constraints                     |
|-------------|------------|---------------------------------|
| Stu_A_id    | BIGINT     | PRIMARY KEY                     |
| A_id        | BIGINT     | NOT NULL, FOREIGN KEY (address.A_id)|
| stu_id      | BIGINT     | NOT NULL, FOREIGN KEY (student.stu_id)|

## Student Table
| Column Name | Data Type  | Constraints     |
|-------------|------------|-----------------|
| stu_id      | BIGINT     | PRIMARY KEY     |
| F_name      | VARCHAR    | NOT NULL        |
| L_name      | VARCHAR    | NOT NULL        |
| F_telephone | VARCHAR(11)| NOT NULL        |
| L_telephone | VARCHAR(11)|                 |
| Birth_date  | DATE       | NOT NULL        |
| img         | TEXT       |                 |

## Professor Table
| Column Name | Data Type  | Constraints                        |
|-------------|------------|------------------------------------|
| P_id        | BIGINT     | PRIMARY KEY                        |
| F_id        | BIGINT     | NOT NULL, FOREIGN KEY (faculty.F_id)|
| D_id        | BIGINT     | NOT NULL, FOREIGN KEY (Department.D_id)|
| F_name      | VARCHAR    | NOT NULL                           |
| L_name      | VARCHAR    | NOT NULL                           |
| age         | VARCHAR(2) | NOT NULL                           |
| salary      | FLOAT      | NOT NULL                           |
| img         | TEXT       |                                    |

## Subject Table
| Column Name | Data Type  | Constraints                       |
|-------------|------------|-----------------------------------|
| sub_id      | BIGINT     | PRIMARY KEY                       |
| sub_name    | VARCHAR    | NOT NULL                          |
| sub_code    | VARCHAR    | NOT NULL                          |
| F_id        | BIGINT     | NOT NULL, FOREIGN KEY (faculty.F_id)|

## Course Table
| Column Name | Data Type  | Constraints                    |
|-------------|------------|--------------------------------|
| C_id        | BIGINT     | PRIMARY KEY                    |
| sub_id      | BIGINT     | NOT NULL, FOREIGN KEY (subject.sub_id)|
| Duration    | VARCHAR(2) | NOT NULL                       |
| P_id        | BIGINT     | NOT NULL, FOREIGN KEY (Professor.P_id)|

## Course_Enrolment Table
| Column Name | Data Type  | Constraints                          |
|-------------|------------|--------------------------------------|
| C_E_id      | BIGINT     | PRIMARY KEY                          |
| C_id        | BIGINT     | NOT NULL, FOREIGN KEY (Course.C_id)  |
| stu_id      | BIGINT     | NOT NULL, FOREIGN KEY (student.stu_id)|

## Exams Table
| Column Name | Data Type  | Constraints                        |
|-------------|------------|------------------------------------|
| E_id        | BIGINT     | PRIMARY KEY                        |
| C_id        | BIGINT     | NOT NULL, FOREIGN KEY (Course.C_id)|
| EXAM_DATE   | DATE       | NOT NULL                           |
| EXAM_TIME   | TIME       | NOT NULL                           |
| EXAM_Duration | VARCHAR(2)| NOT NULL                           |
