#* CREATE TABLE Faculty(
   * F_id BIGINT PRIMARY KEY NOT NULL,
   * F_name VARCHAR NOT NULL  );

#* CREATE TABLE Department(
   * D_id BIGINT PRIMARY KEY NOT NULL,
   * D_name VARCHAR NOT NULL,
   * F_id BIGINT  NOT NULL REFERENCES  faculty(F_id);
   
#* CREATE TABLE Address(
   * A_id BIGINT PRIMARY KEY NOT NULL,
   * Gvernorate VARCHAR NOT NULL ,
   * city VARCHAR(15) NOT NULL ,
   * line1 VARCHAR NOT NULL ,
   * line2 VARCHAR  );
   
#* CREATE TABLE Student_Address(
   * Stu_A_id BIGINT PRIMARY KEY  NOT NULL,
   * A_id BIGINT NOT NULL REFERENCES address(A_id),
   * stu_id BIGINT NOT NULL REFERENCES student(stu_id);
   
#* CREATE TABLE Student(
   * stu_id BIGINT PRIMARY KEY NOT NULL,
   * F_name VARCHAR NOT NULL ,
   * L_name VARCHAR Not NULL,
   * F_telephone VARCHAR(11) NOT NULL, 
   * L_telephone VARCHAR(11),
   * Birth_date DATE NOT NULL ,
   * img TEXT );
   
#* CREATE TABLE Professor(
   * P_id BIGINT PRIMARY KEY NOT NULL,
   * F_id BIGINT NOT NULL REFERENCES faculty(F_id),
   * D_id BIGINT NOT NULL REFERENCES Department(D_id),
   * F_name VARCHAR NOT NULL ,
   * L_name VARCHAR NOT NULL,
   * age VARCHAR(2) NOT NULL,
   * salary FLOAT NOT NULL,
   * img TEXT );
   
#* CREATE TABLE Subject(
   * sub_id BIGINT PRIMARY KEY NOT NULL,
   * sub_name VARCHAR NOT NULL,
   * sub_code VARCHAR NOT NULL,
   * F_id BIGINT NOT NULL REFERENCES faculty(F_id);
   
#* CREATE TABLE Course(
   * C_id BIGINT PRIMARY KEY NOT NULL,
   * sub_id BIGINT NOT NULL REFERENCES subject(sub_id),
   * Duration VARCHAR(2) NOT NULL,
   * P_id BIGINT NOT NULL REFERENCES Professor(P_id);
   
#* CREATE TABLE Course_Enrolment(
   * C_E_id BIGINT PRIMARY KEY NOT NULL,
   * C_id BIGINT NOT NULL REFERENCES Course(C_id),
   * stu_id BIGINT NOT NULL REFERENCES student(stu_id) );
   
#* CREATE TABLE Exams(
   * E_id BIGINT PRIMARY KEY NOT NULL,
   * C_id BIGINT NOT NULL REFERENCES Course(C_id),
   * EXAM_DATE DATE NOT NULL,
   * EXAM_TIME TIME NOT NULL,
   * EXAM_Duration VARCHAR(2) NOT NULL);
   
