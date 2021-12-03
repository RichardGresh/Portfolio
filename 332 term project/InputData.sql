INSERT INTO PROFESSOR(Prof_SSN, Prof_Name, Prof_Title, Prof_Sex, Prof_Salary, Prof_Area_Code, Prof_7_Digits, Prof_City, Prof_State, Prof_Zip_Code, Prof_Street_Address)
VALUES(687493044, 'Halt Carrick', 'Dr.', 'M', 98345, '714', '441-9706', 'Fullerton','CA', '92632', '3410 Liberty Avenue');

INSERT INTO PROFESSOR(Prof_SSN, Prof_Name, Prof_Title, Prof_Sex, Prof_Salary, Prof_Area_Code, Prof_7_Digits, Prof_City, Prof_State, Prof_Zip_Code, Prof_Street_Address)
VALUES(603376989, 'Thom Merrilin', 'Dr.', 'M', 101329, '714', '853-3886', 'Fullerton', 'CA', '92831', '470 Juniper Drive' );

INSERT INTO PROFESSOR(Prof_SSN, Prof_Name, Prof_Title, Prof_Sex, Prof_Salary, Prof_Area_Code, Prof_7_Digits, Prof_City, Prof_State, Prof_Zip_Code, Prof_Street_Address)
VALUES(165569841, 'Moiraine Damodred', 'Mr.', 'F', 108390, '308', '550-2799', 'Fullerton', 'CA', '68638', '3127 Kyle Street');


INSERT INTO DEPARTMENT(Depart_Num, Depart_Name, Depart_Phone, Depart_Office_Location, Depart_Chairman_SSN)
VALUES ('59688', 'Computer Science', '657-278-3700','CS-522', 687493044);

INSERT INTO DEPARTMENT(Depart_Num, Depart_Name, Depart_Phone, Depart_Office_Location, Depart_Chairman_SSN)
VALUES ('99759', 'Electrical Engineering', '657-278-7162', 'E-100a', 165569841);

INSERT INTO COURSE(Course_Num, Course_Units, Course_Title, Course_Text_Book, Course_Department_Num)
VALUES('CPSC 362', '3', 'Foundations of Software Engineering', 'Software Engineering: A Practical Approach, by Pressman, 8th Edition','59688');

INSERT INTO COURSE(Course_Num, Course_Units, Course_Title, Course_Text_Book, Course_Department_Num)
VALUES ('CPSC 335', '3', 'Algorithm Engineering', 'Algorithm Design in Three Acts, Kevin Wortman, Beta Edition','59688');

INSERT INTO COURSE(Course_Num, Course_Units, Course_Title, Course_Text_Book, Course_Department_Num)
VALUES ('CPSC 386', '3', 'Introduction to Game Design and Production', 'Half-Real: Video Games between Real Rules and Fictional Worlds','59688');

INSERT INTO COURSE(Course_Num, Course_Units, Course_Title, Course_Text_Book, Course_Department_Num)
VALUES ('EGCP 450', '4', 'Embedded Processors', 'Introduction to the MSP432 MicroController Embedded Systems','99759');


INSERT INTO SECTION(Sect_Num, Sect_Course_Num, Sect_Num_Of_Seats, Sect_Classroom, Sect_Meeting_Days, Sect_Begin_Time, Sect_End_Time, Sect_Prof_SSN)
VALUES(13867, 'CPSC 362', 33, 'WEB', 'MW' , '3:00pm', '4:15pm', 687493044);

INSERT INTO SECTION(Sect_Num, Sect_Course_Num, Sect_Num_Of_Seats, Sect_Classroom, Sect_Meeting_Days, Sect_Begin_Time, Sect_End_Time, Sect_Prof_SSN)
VALUES(25317, 'CPSC 362', 26, 'WEB', 'TTH' , '1:30pm', '2:45pm', 687493044);

INSERT INTO SECTION(Sect_Num, Sect_Course_Num, Sect_Num_Of_Seats, Sect_Classroom, Sect_Meeting_Days, Sect_Begin_Time, Sect_End_Time, Sect_Prof_SSN)
VALUES(13772, 'CPSC 335', 41, 'WEB', 'TTH', '5:45pm', '7:00pm',165569841);

INSERT INTO SECTION(Sect_Num, Sect_Course_Num, Sect_Num_Of_Seats, Sect_Classroom, Sect_Meeting_Days, Sect_Begin_Time, Sect_End_Time, Sect_Prof_SSN)
VALUES(13794, 'CPSC 335', 37, 'WEB', 'TTH', '3:00pm', '4:15pm',165569841);

INSERT INTO SECTION(Sect_Num, Sect_Course_Num, Sect_Num_Of_Seats, Sect_Classroom, Sect_Meeting_Days, Sect_Begin_Time, Sect_End_Time, Sect_Prof_SSN)
VALUES(11934, 'CPSC 335', 21, 'WEB', 'MW', '9:30am', '10:45am', 687493044);

INSERT INTO SECTION(Sect_Num, Sect_Course_Num, Sect_Num_Of_Seats, Sect_Classroom, Sect_Meeting_Days, Sect_Begin_Time, Sect_End_Time, Sect_Prof_SSN)
VALUES(13575, 'CPSC 386', 29, 'WEB', 'MW', '5:15pm', '6:45pm', 165569841);

INSERT INTO SECTION(Sect_Num, Sect_Course_Num, Sect_Num_Of_Seats, Sect_Classroom, Sect_Meeting_Days, Sect_Begin_Time, Sect_End_Time, Sect_Prof_SSN)
VALUES(19743, 'CPSC 386', 35, 'WEB', 'TTH', '10:00am', '11:15pm', 687493044);

INSERT INTO SECTION(Sect_Num, Sect_Course_Num, Sect_Num_Of_Seats, Sect_Classroom, Sect_Meeting_Days, Sect_Begin_Time, Sect_End_Time, Sect_Prof_SSN)
VALUES(10314, 'EGCP 450', 36, 'RGC 021', 'MW', '1:00pm', '2:15pm', 603376989);

INSERT INTO STUDENT(Stud_CWID, Stud_FName, Stud_LName, Stud_Address, Stud_Phone, Stud_Depart_Num)
VALUES (210394136, 'Mat', 'Cauthon', '4059 Elk Street Fullerton, CA 93632', '714-702-9544', '59688');

INSERT INTO STUDENT(Stud_CWID, Stud_FName, Stud_LName, Stud_Address, Stud_Phone, Stud_Depart_Num)
VALUES (558710559, 'Rand', 'al Thor', '4333 Denver Avenue Fullerton, CA 9362', '714-294-4551', '99759');

INSERT INTO STUDENT(Stud_CWID, Stud_FName, Stud_LName, Stud_Address, Stud_Phone, Stud_Depart_Num)
VALUES (008415470, 'Egwene', 'al Vere', '3580 Paradise Lane Fullerton, CA 93632', '714-853-5238', '59688');

INSERT INTO STUDENT(Stud_CWID, Stud_FName, Stud_LName, Stud_Address, Stud_Phone, Stud_Depart_Num)
VALUES (237644461, 'Perrin', 'Aybara','3149 Murphy Court Fullerton, CA 93632', '714-770-4995','59688');

INSERT INTO STUDENT(Stud_CWID, Stud_FName, Stud_LName, Stud_Address, Stud_Phone, Stud_Depart_Num)
VALUES (654164732, 'Will', 'Treaty', '2626 Denver Avenue Fullerton, CA 93632', '715-726-2599','99759');

INSERT INTO STUDENT(Stud_CWID, Stud_FName, Stud_LName, Stud_Address, Stud_Phone, Stud_Depart_Num)
VALUES (877989890, 'Horace', 'Altman', '682 Cardinal Lane Fullerton, CA 58441', '701-334-9578', '59688');

INSERT INTO STUDENT(Stud_CWID, Stud_FName, Stud_LName, Stud_Address, Stud_Phone, Stud_Depart_Num)
VALUES (262653114, 'Gilan', 'Dalby', '984 Sycamore Fork Road Fullerton, CA 58441', '701-900-7291','99759');

INSERT INTO STUDENT(Stud_CWID, Stud_FName, Stud_LName, Stud_Address, Stud_Phone, Stud_Depart_Num)
VALUES (282838570, 'Evanlyn', 'Wheeler', '1239 Brown Bear Drive Fullerton, CA 93632', '714-498-3220', '59688');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(210394136, 13867, 'CPSC 362', 'B+');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(210394136, 13794, 'CPSC 335', 'A-');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(210394136, 13575, 'CPSC 386', 'B');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(210394136, 10314, 'EGCP 450', 'C+');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(558710559, 19743, 'CPSC 386', 'A');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(558710559, 10314, 'EGCP 450', 'C-');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(558710559, 25317, 'CPSC 362', 'B-');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(008415470, 13867, 'CPSC 362', 'D-');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(008415470, 11934, 'CPSC 335', 'F');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(008415470, 13575, 'CPSC 386', 'A-');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(008415470, 10314, 'EGCP 450', 'F');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(237644461, 13772, 'CPSC 335', 'C+');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(237644461, 25317, 'CPSC 362', 'A');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(237644461, 19743, 'CPSC 386', 'B+');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(654164732, 13867, 'CPSC 362', 'A-');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(654164732, 13575, 'CPSC 386', 'D+');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(654164732, 10314, 'EGCP 450', 'A-');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(877989890, 19743, 'CPSC 386', 'C+');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(877989890, 25317, 'CPSC 362', 'B');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(877989890, 11934, 'CPSC 335', 'B-');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(262653114, 13772, 'CPSC 335', 'A');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(262653114, 10314, 'EGCP 450', 'B');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(262653114, 13575, 'CPSC 386', 'D+');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(282838570, 13575, 'CPSC 386', 'C');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(282838570, 13772, 'CPSC 335', 'A-');

INSERT INTO ENROLLMENT(Enroll_CWID, Enroll_Sect_Num, Enroll_Course_Num, Grade)
VALUES(282838570, 25317, 'CPSC 362','A');


INSERT INTO MINOR(Minor_Depart_Num, Minor_CWID)
VALUES('99759', 008415470);

INSERT INTO MINOR(Minor_Depart_Num, Minor_CWID)
VALUES('99759', 210394136);

INSERT INTO MINOR(Minor_Depart_Num, Minor_CWID)
VALUES('59688', 558710559);

INSERT INTO MINOR(Minor_Depart_Num, Minor_CWID)
VALUES('59688', 654164732);

INSERT INTO MINOR(Minor_Depart_Num, Minor_CWID)
VALUES('59688', 262653114);


INSERT INTO DEGREE(Deg_Degree, Deg_Professor_SSN)
VALUES('B.S Computer Science', 687493044);

INSERT INTO DEGREE(Deg_Degree, Deg_Professor_SSN)
VALUES('M.S Computer Science', 687493044);

INSERT INTO DEGREE(Deg_Degree, Deg_Professor_SSN)
VALUES('Ph.D Computer Science', 687493044);

INSERT INTO DEGREE(Deg_Degree, Deg_Professor_SSN)
VALUES('B.S Computer Engineering', 165569841);

INSERT INTO DEGREE(Deg_Degree, Deg_Professor_SSN)
VALUES('M.S Computer Science', 165569841);

INSERT INTO DEGREE(Deg_Degree, Deg_Professor_SSN)
VALUES('Ph.D Computer Science', 165569841);

INSERT INTO DEGREE(Deg_Degree, Deg_Professor_SSN)
VALUES('B.S Physics', 603376989);

INSERT INTO DEGREE(Deg_Degree, Deg_Professor_SSN)
VALUES('M.S Electrical Engineering', 603376989);


INSERT INTO PREREQUISITES(Cur_Course_Num,Prereq_Course_Num)
VALUES('CPSC 362','CPSC 335');

INSERT INTO PREREQUISITES(Cur_Course_Num,Prereq_Course_Num)
VALUES('CPSC 386', 'CPSC 335');

INSERT INTO PREREQUISITES(Cur_Course_Num,Prereq_Course_Num)
VALUES('EGCP 450', 'CPSC 362');
