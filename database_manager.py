import mysql.connector

class DatabaseManager:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Swarajp@123',
            database='Student_Grades_Data'
        )
        self.cursor = self.conn.cursor()

    def add_student(self, student_id, name):
        query = "INSERT INTO student(student_id, name) VALUES(%s, %s)"
        self.cursor.execute(query, (student_id, name))
        self.conn.commit()

    def enter_marks(self, student_id, subject, marks):
        query = "INSERT INTO marks(student_id, subject, marks) VALUES(%s, %s, %s)"
        self.cursor.execute(query, (student_id, subject, marks))
        self.conn.commit()

    def get_student_name(self, student_id):
        query = "SELECT name FROM student WHERE student_id = %s"
        self.cursor.execute(query, (student_id,))
        return self.cursor.fetchone()

    def get_student_marks(self, student_id):
        query = "SELECT subject, marks FROM marks WHERE student_id = %s"
        self.cursor.execute(query, (student_id,))
        return self.cursor.fetchall()
