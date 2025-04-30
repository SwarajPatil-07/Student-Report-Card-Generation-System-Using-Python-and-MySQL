CREATE DATABASE Student_Grades_Data;
USE Student_Grades_Data;

CREATE TABLE student (
			student_id INT PRIMARY KEY,
			name VARCHAR(100)
);

CREATE TABLE marks (
			id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT, 
            subject VARCHAR(50), 
            marks INT, 
            FOREIGN KEY(student_id) REFERENCES student(student_id)
);

