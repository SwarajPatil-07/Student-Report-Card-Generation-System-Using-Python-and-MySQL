**Student Report Card Generation System Using Python and MySQL**

This project is a web-based application designed to manage student records and generate academic report cards. Built with Python (Flask) for the backend, MySQL for data storage, and HTML/CSS for the frontend, this system allows users to add students, enter their marks, and view detailed reports including total, percentage, and grade.


🔧 Features

- 🎓 Add new student records
- 📝 Enter subject-wise marks for each student
- 📊 Automatically calculate total marks, percentage, and grades
- 📋 Generate and display detailed report cards
- 🌐 User-friendly web interface styled with CSS


🛠️ Technologies Used

- Python 3
- Flask
- MySQL
- HTML & CSS


🗃️ Database Schema

Database: `student_grades_data`

Table: `student`
| Column Name | Data Type | Description            |
|-------------|------------|------------------------|
| student_id  | INT        | Primary Key            |
| name        | VARCHAR    | Name of the student    |

Table: `marks`
| Column Name | Data Type | Description                      |
|-------------|------------|----------------------------------|
| id          | INT (AUTO_INCREMENT) | Primary Key          |
| student_id  | INT        | Foreign Key (from `student`)     |
| subject     | VARCHAR    | Subject name                     |
| marks       | INT        | Marks obtained                   |



🚀 How to Run the Project

1. Clone the repository

   git clone https://github.com/SwarajPatil-07/Student-Report-Card-Generation-System-Using-Python-and-MySQL
   cd student-report-card-system
   

2. Set up the virtual environment (optional but recommended) 
   
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   

3. Install dependencies
   
   pip install flask mysql-connector-python
   

4. Create the MySQL database
   Use the following SQL commands:
   
   CREATE DATABASE student_grades;

   USE student_grades;

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
   

5. Run the Flask app
   
   python app.py
   

6. Visit in browser  
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.


📸 Screenshots

![Screenshot 2025-05-01 050657](https://github.com/user-attachments/assets/1554b2db-5669-43e6-9404-41e26498ccac)

![Screenshot 2025-05-01 051134](https://github.com/user-attachments/assets/d2ab8732-ebc9-41e6-abc9-29fd65f1eed2)

![Screenshot 2025-05-01 051152](https://github.com/user-attachments/assets/55601d5a-7e44-4ad2-af8b-e1c50e51a6b6)

![Screenshot 2025-05-01 050737](https://github.com/user-attachments/assets/80e3aae3-cd45-4b86-8a73-1a33034b94c6)

![Screenshot 2025-05-01 051238](https://github.com/user-attachments/assets/8384043e-5e6c-4f4c-8d84-b2ec0c31d86c)

📚 Future Improvements

- Add student authentication/login
- Enable editing and deleting records
- Export report cards as PDF
- Add subject weightage or grading scale customization


