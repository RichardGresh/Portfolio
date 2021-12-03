CREATE TABLE PROFESSOR(
   Prof_SSN INT NOT NULL,
   Prof_Name VARCHAR(40) NOT NULL,
   Prof_Title VARCHAR(10) NOT NULL,
   Prof_Sex enum('M', 'F') NOT NULL,
   Prof_Salary INT NOT NULL,
   Prof_Area_Code VARCHAR(3),
   Prof_7_Digits VARCHAR(9) NOT NULL,
   Prof_City VARCHAR(60) NOT NULL,
   Prof_State VARCHAR(2) NOT NULL,
   Prof_Zip_Code VARCHAR(5) NOT NULL,
   Prof_Street_Address VARCHAR(70) NOT NULL,
   PRIMARY KEY(Prof_SSN));


CREATE TABLE DEPARTMENT(
   Depart_Num VARCHAR(12) NOT NULL,
   Depart_Name VARCHAR(30) NOT NULL,
   Depart_Phone VARCHAR(12) NOT NULL,
   Depart_Office_Location VARCHAR(30) NOT NULL,
   Depart_Chairman_SSN INT,
   PRIMARY KEY(Depart_Num),
   FOREIGN KEY(Depart_Chairman_SSN) REFERENCES PROFESSOR(Prof_SSN));


CREATE TABLE STUDENT(
   Stud_CWID INT NOT NULL,
   Stud_FName VARCHAR(35) NOT NULL,
   Stud_LName VARCHAR(35) NOT NULL,
   Stud_Address VARCHAR(60) NOT NULL,
   Stud_Phone VARCHAR(12) NOT NULL,
   Stud_Depart_Num VARCHAR(12),
   PRIMARY KEY(Stud_CWID),
   FOREIGN KEY(Stud_Depart_Num) REFERENCES DEPARTMENT(Depart_Num));
   




CREATE TABLE COURSE(
   Course_Num VARCHAR(15) NOT NULL,
   Course_Units ENUM('3','4','5') NOT NULL,
   Course_Title VARCHAR(60) NOT NULL,
   Course_Text_Book VARCHAR(90) NOT NULL,
   Course_Department_Num VARCHAR(12),
   PRIMARY KEY(Course_Num),
   FOREIGN KEY(Course_Department_Num) REFERENCES DEPARTMENT(Depart_Num));


CREATE TABLE SECTION(
   Sect_Num INT NOT NULL,
   Sect_Course_Num VARCHAR(15),
   Sect_Num_Of_Seats INT NOT NULL,
   Sect_Classroom VARCHAR(30) NOT NULL,
   Sect_Meeting_Days VARCHAR(10) NOT NULL,
   Sect_Begin_Time VARCHAR(10) NOT NULL,
   Sect_End_Time VARCHAR(10) NOT NULL,
   Sect_Prof_SSN INT,
   PRIMARY KEY(Sect_Num,Sect_Course_Num),
   FOREIGN KEY(Sect_Course_Num) REFERENCES COURSE(Course_Num),
   FOREIGN KEY(Sect_Prof_SSN) REFERENCES PROFESSOR(Prof_SSN));

CREATE TABLE ENROLLMENT(
   Enroll_CWID INT,
   Enroll_Sect_Num INT,
   Enroll_Course_Num VARCHAR(15),
   Grade ENUM('A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'),
   PRIMARY KEY(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num),
   FOREIGN KEY(Enroll_CWID) REFERENCES STUDENT(Stud_CWID),
   FOREIGN KEY(Enroll_Sect_Num) REFERENCES SECTION(Sect_Num),
   FOREIGN KEY(Enroll_Course_Num) REFERENCES COURSE(Course_Num));
   


CREATE TABLE MINOR(
   Minor_Depart_Num VARCHAR(12),
   Minor_CWID INT,
   PRIMARY KEY(Minor_Depart_Num, Minor_CWID),
   FOREIGN KEY(Minor_Depart_Num) REFERENCES DEPARTMENT(Depart_Num),
   FOREIGN KEY(Minor_CWID) REFERENCES STUDENT(Stud_CWID));
   


CREATE TABLE DEGREE(
   Deg_Degree VARCHAR(30) NOT NULL,
   Deg_Professor_SSN INT,
   PRIMARY KEY(Deg_Degree, Deg_Professor_SSN),
   FOREIGN KEY(Deg_Professor_SSN) REFERENCES PROFESSOR(Prof_SSN));


CREATE TABLE PREREQUISITES(
   Cur_Course_Num VARCHAR(15),
   Prereq_Course_Num VarChar(15),
   PRIMARY KEY(Cur_Course_Num, Prereq_Course_Num),
   FOREIGN KEY(Cur_Course_Num) REFERENCES COURSE (Course_Num),
   FOREIGN KEY(Prereq_Course_Num) REFERENCES COURSE (Course_Num));


