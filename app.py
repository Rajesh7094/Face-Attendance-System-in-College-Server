from flask import Flask, render_template, request, redirect, url_for, jsonify
from attendance import mark_attendance, view_attendance_records
from face_registration import register_student_face
from email_notification import send_absentee_report
import os
import json

app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# View Attendance
@app.route('/view_attendance')
def view_attendance():
    attendance_data = view_attendance_records()
    return render_template('view_attendance.html', attendance_data=attendance_data)

# Start Attendance
@app.route('/start_attendance', methods=['POST'])
def start_attendance():
    lab_id = request.form['lab_id']
    period = int(request.form['period'])
    mark_attendance(lab_id, period)
    return redirect(url_for('index'))

# Register Student Face
@app.route('/register_face', methods=['GET', 'POST'])
def register_face():
    if request.method == 'POST':
        student_id = request.form['student_id']
        name = request.form['name']
        year = int(request.form['year'])
        department = request.form['department']
        register_student_face(student_id, name, year, department)
        return redirect(url_for('index'))
    return render_template('add_student.html')

# API to fetch timetable
@app.route('/get_timetable/<lab_id>', methods=['GET'])
def get_timetable(lab_id):
    with open("data/lab_timetables.json") as f:
        timetable = json.load(f)
    return jsonify(timetable.get(lab_id, []))

if __name__ == '__main__':
    app.run(debug=True)
