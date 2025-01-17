import pandas as pd
import os
from datetime import datetime

def load_students(year, department):
    filename = f"data/student_details/{year}_year_{department}.csv"
    if os.path.exists(filename):
        return pd.read_csv(filename)
    return pd.DataFrame()

def mark_attendance(lab_id, period):
    # Load timetable
    with open("data/lab_timetables.json", "r") as f:
        timetable = json.load(f)
    
    lab_schedule = timetable.get(lab_id, [])
    for session in lab_schedule:
        if session["period"] == period:
            year = session["year"]
            department = session["department"]
            students = load_students(year, department)
            
            # Generate attendance record
            attendance_file = f"data/attendance_records/{datetime.now().strftime('%Y%m%d')}_lab_{lab_id}_period_{period}.csv"
            students["Attendance"] = "Present"
            students["Timestamp"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            students.to_csv(attendance_file, index=False)

def view_attendance_records():
    attendance_path = "data/attendance_records/"
    files = os.listdir(attendance_path)
    records = []
    for file in files:
        df = pd.read_csv(os.path.join(attendance_path, file))
        records.append(df)
    return records
