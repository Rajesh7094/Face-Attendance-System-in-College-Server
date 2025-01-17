import os

def register_student_face(student_id, name, year, department):
    face_dir = f"data/face_data/{student_id}/"
    os.makedirs(face_dir, exist_ok=True)
    print(f"Face data for {name} ({student_id}) registered successfully.")
