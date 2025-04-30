from flask import Flask, render_template, request, redirect, url_for
from database_manager import DatabaseManager

app = Flask(__name__)
db = DatabaseManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        student_id = int(request.form['student_id'])
        name = request.form['name']
        db.add_student(student_id, name)
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/enter_marks', methods=['GET', 'POST'])
def enter_marks():
    if request.method == 'POST':
        student_id = int(request.form['student_id'])
        subjects = request.form.getlist('subject')
        marks_list = request.form.getlist('marks')
        for subject, marks in zip(subjects, marks_list):
            db.enter_marks(student_id, subject, int(marks))
        return redirect(url_for('index'))
    return render_template('enter_marks.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    student_data = None
    if request.method == 'POST':
        student_id = int(request.form['student_id'])
        name = db.get_student_name(student_id)
        if name:
            marks = dict(db.get_student_marks(student_id))
            total = sum(marks.values())
            percentage = total / len(marks)
            grade = (
                "A" if percentage >= 90 else
                "B" if percentage >= 75 else
                "C" if percentage >= 60 else
                "D" if percentage >= 45 else "F"
            )
            student_data = {
                'id': student_id,
                'name': name[0],
                'marks': marks,
                'total': total,
                'percentage': round(percentage, 2),
                'grade': grade
            }
    return render_template('report.html', student=student_data)

if __name__ == '__main__':
    app.run(debug=True)
