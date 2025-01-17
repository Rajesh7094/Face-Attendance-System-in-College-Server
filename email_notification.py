import smtplib
from email.mime.text import MIMEText


# Function to send absentee report emails
def send_absentee_report(absentees, recipient_emails):
    """
    Sends absentee reports to multiple email recipients (e.g., HODs and Vice Principal).

    Parameters:
    - absentees: List of absent students (e.g., ["John Doe", "Jane Smith"])
    - recipient_emails: Dictionary of recipients with department names as keys and email addresses as values

    Example of recipient_emails:
    {
        "HOD_CSE": "hod_cse@example.com",
        "HOD_AI&DS": "hod_aids@example.com",
        "Vice_Principal": "vice_principal@example.com"
    }
    """

    # Email subject and body
    subject = "Absentee Report"
    body = f"Absentees: {', '.join(absentees)}"

    # SMTP Configuration (Add your email credentials here)
    smtp_server = "smtp.example.com"  # Replace with your SMTP server (e.g., smtp.gmail.com)
    smtp_port = 587  # Usually 587 for TLS
    sender_email = "your_email@example.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password or app password

    # Create the email message
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in with sender's email credentials

            # Send email to each recipient in the dictionary
            for dept, recipient_email in recipient_emails.items():
                msg["To"] = recipient_email  # Set recipient email
                server.sendmail(sender_email, [recipient_email], msg.as_string())  # Send email
                print(f"Email sent to {dept} ({recipient_email}) successfully!")

    except Exception as e:
        print(f"Error while sending email: {e}")

# Example Usage (Identify where to add all mail IDs)
if __name__ == "__main__":
    # List of absentees (Replace with actual absentee names)
    absentees = ["John Doe", "Jane Smith", "Alice Brown"]

    # Add HOD and Vice Principal email IDs here
    recipient_emails = {
        "HOD_CSE": "hod_cse@example.com",       # Replace with HOD of CSE email
        "HOD_AI&DS": "hod_aids@example.com",   # Replace with HOD of AI&DS email
        "HOD_Mech": "hod_mech@example.com",    # Replace with HOD of Mechanical email
        "Vice_Principal": "vice_principal@example.com"  # Replace with Vice Principal email
    }

    # Send absentee report
    send_absentee_report(absentees, recipient_emails)
