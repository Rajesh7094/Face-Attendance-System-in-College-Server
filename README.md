# Face Recognition Attendance System

## **Project Overview**
This is a Face Recognition Attendance System designed for a college laboratory environment. The system automates the process of marking attendance using facial recognition technology and incorporates features such as student registration, absentee notification, and attendance logs. While the project was successfully implemented in code, the college server crashed before deployment, so the system was not run live. This repository is hosted on GitHub for future use and improvements.

---

## **College Requirements**
The attendance system was designed to meet the following requirements:

1. **Daily Attendance Tracking**:
   - Handles attendance for approximately 200 students daily.
   - Logs attendance for each period (40-50 minutes, customizable).

2. **Face Detection and Recognition**:
   - Automates face detection with a 10-minute grace period at the start of each period.
   - Disables detection after the grace period until the next period begins.

3. **Manual Entry Support**:
   - Allows staff to manually add students by capturing their face data, register number, and department.
   - Handles late entries by logging register number, entry time, and duration in the lab.

4. **Attendance Management**:
   - Automatically resets attendance logs for each new period.
   - Sends absentee details to the respective department HOD via email after each period.
   - Sends a complete absentee report to the Vice Principal at the end of the day.

5. **Data Security and Access Control**:
   - Staff and admin roles for accessing and modifying attendance.
   - Lab-specific IDs and passwords for viewing attendance records without modification rights.

---

## **Project Features**

1. **Face Detection and Registration**:
   - Students' faces are registered with their name, register number, and department.
   - Captured data is stored for future recognition.

2. **Attendance Logging**:
   - Automated attendance marking using face recognition.
   - Stores attendance data in Excel files for each period.

3. **Email Notifications**:
   - Sends absentee notifications to HODs after each period.
   - Sends a consolidated absentee report to the Vice Principal.

4. **Flexible Deployment**:
   - Designed to run on a local system or deploy on a server.

---

## **Directory Structure**
```plaintext
attendance_system/
├── app.py                     # Main Flask application
├── attendance.py              # Face detection and attendance logic
├── email_notification.py      # Email notification script
├── face_registration.py       # Script for registering new students
├── requirements.txt           # Python dependencies
├── static/                    # Static files
│   ├── css/
│   │   └── style.css          # Custom CSS styles
│   ├── js/
│   │   └── script.js          # Custom JavaScript
│   ├── images/
│   │   └── logo.png           # Application logo
│   └── fonts/
│       └── custom-font.woff   # Custom fonts
├── templates/                 # HTML templates
│   ├── base.html              # Base template
│   ├── index.html             # Main page
│   ├── attendance.html        # Attendance page
│   └── register.html          # Registration page
├── student_data/              # Student registration and attendance data
│   ├── student_details.csv    # Student registration data
│   └── attendance_logs/       # Folder for storing attendance logs
└── README.md                  # Project documentation
```

---

## **Setup and Requirements**

### **System Requirements**
- **Hardware**:
  - Intel Xeon server (or equivalent), minimum 16GB RAM, 1TB SSD.
  - GPU recommended for faster face detection.
- **Software**:
  - Python 3.13.0
  - Flask (for web application)
  - OpenCV (for face detection)
  - Pandas (for data management)
  - Gunicorn (for production deployment)
  - Nginx (for reverse proxy and static file serving)

### **Steps to Set Up Locally**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Rajesh7094/Face-Attendance-System-in-College-Server.git
   cd attendance_system
   ```

2. **Install Dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python3 app.py
   ```
   Access the application at `http://127.0.0.1:5000/`.

4. **Deploy on Server** (Optional):
   - Use Gunicorn and Nginx for production deployment (instructions in the project).

---

## **Challenges Faced**
- The college server (Xeon, 32GB RAM) crashed before the project could be deployed. As a result, the system remains untested in a real-world environment.
- This project is hosted on GitHub to preserve the work and facilitate future use.

---

## **Future Improvements**
1. **Server Deployment**:
   - Deploy and test the system on a stable server.

2. **Enhance Face Recognition**:
   - Improve accuracy with advanced algorithms or pre-trained models.

3. **UI/UX Improvements**:
   - Enhance the web interface for better usability.

4. **Scalability**:
   - Extend the system to support multiple departments or campuses.

---

Feel free to contribute to the project or adapt it to suit your requirements. For any questions or issues, please open a GitHub issue.
