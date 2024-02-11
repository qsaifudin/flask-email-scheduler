# src/email_scheduler.py
from flask import current_app
import threading
import time
from ..db.email import db, Email, ArchiveEmail
from datetime import datetime
import pytz
from flask import jsonify

# Flag to control the email scheduler
email_scheduler_running = False
timezone_sg = pytz.timezone("Asia/Singapore")


# Start the email scheduler in a separate thread
def start_email_scheduler():
    global email_scheduler_running
    if not email_scheduler_running:
        threading.Thread(
            target=email_scheduler_task,
            args=(current_app._get_current_object(),),
            daemon=True,
        ).start()


# Stop the email scheduler
def stop_email_scheduler():
    global email_scheduler_running
    email_scheduler_running = False


def email_scheduler_task(app):
    global email_scheduler_running
    email_scheduler_running = True
    # Function that continuously checks for the time and sends necessary emails
    with app.app_context():
        while email_scheduler_running:
            try:
                emails = Email.query.all()
                print(emails)
                # Process each email
                process_emails(emails)

            except Exception as e:
                print(f"Error occurred while processing all emails: {e}")

            # Send emails as needed
            print("Checking for emails...")
            time.sleep(5)  # Example: Check every 5 second


def process_emails(emails):
    try:
        # Iterate through each email
        for email in emails:
            # Convert to UTC+8 timezone
            current_time_sg = (
                datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(timezone_sg)
            )
            email_timestamp_sg = email.timestamp.astimezone(timezone_sg)

            if email_timestamp_sg <= current_time_sg:
                # Move the email to the archive table
                archive_email = ArchiveEmail(
                    event_id=email.event_id,
                    email_subject=email.email_subject,
                    email_content=email.email_content,
                    timestamp=email.timestamp,
                )

                db.session.add(archive_email)
                db.session.commit()

                db.session.delete(email)
                db.session.commit()

                # Send the email (implement your email sending logic here)
                print(f"Sending email with subject: {email.email_subject}")

    except Exception as e:
        print(f"Error occurred while processing emails: {e}")


def get_scheduler_status():
    return jsonify({"status": email_scheduler_running}), 200
