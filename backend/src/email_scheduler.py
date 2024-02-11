# src/email_scheduler.py

import threading
import time

# Flag to control the email scheduler
email_scheduler_running = False

def email_scheduler_task():
    global email_scheduler_running
    email_scheduler_running = True
    # Function that continuously checks for the time and sends necessary emails
    while email_scheduler_running:
        # Implement the logic to check for emails to send based on timestamp
        # Send emails as needed
        print("Checking for emails...")
        time.sleep(5)  # Example: Check every minute

# Start the email scheduler in a separate thread
def start_email_scheduler():
    global email_scheduler_running
    if not email_scheduler_running:
        threading.Thread(target=email_scheduler_task, daemon=True).start()

# Stop the email scheduler
def stop_email_scheduler():
    global email_scheduler_running
    email_scheduler_running = False
