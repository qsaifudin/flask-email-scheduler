# src/email_logic.py
from flask import jsonify
from ..db.email import db, Email,ArchiveEmail
from datetime import datetime
from .email_scheduler import start_email_scheduler, stop_email_scheduler

def save_email(data):
    event_id = data.get("event_id")
    email_subject = data.get("email_subject")
    email_content = data.get("email_content")
    timestamp = datetime.strptime(data.get("timestamp"), "%d %b %Y %H:%M")

    # Check if the email with the given event_id already exists
    existing_email = Email.query.filter_by(event_id=event_id).first()
    if existing_email:
        return jsonify({"error": "Email with this event_id already exists"}), 400

    email = Email(
        event_id=event_id,
        email_subject=email_subject,
        email_content=email_content,
        timestamp=timestamp,
    )
    db.session.add(email)
    db.session.commit()

    response = {
        "data": data,
        "status": "success",
        "message": "Email saved successfully",
    }
    return jsonify(response), 201


def get_all_emails():
    emails = Email.query.order_by(Email.event_id.desc()).all()
    email_data = [
        {
            "event_id": email.event_id,
            "email_subject": email.email_subject,
            "email_content": email.email_content,
            "timestamp": email.timestamp.strftime("%d %b %Y %H:%M"),
        }
        for email in emails
    ]
    response = {
        "status": "success",
        "message": "Retrieved all emails successfully",
        "data": email_data,
    }
    return jsonify(response), 200

def get_all_archived__emails():
    emails = ArchiveEmail.query.order_by(ArchiveEmail.event_id.desc()).all()
    email_data = [
        {
            "event_id": email.event_id,
            "email_subject": email.email_subject,
            "email_content": email.email_content,
            "timestamp": email.timestamp.strftime("%d %b %Y %H:%M"),
        }
        for email in emails
    ]
    response = {
        "status": "success",
        "message": "Retrieved all emails successfully",
        "data": email_data,
    }
    return jsonify(response), 200

def toggle_email_scheduler(enabled):
    if enabled:
        start_email_scheduler()
        message = "Email scheduler started."
    else:
        stop_email_scheduler()
        message = "Email scheduler stopped."

    return jsonify({"message": message}), 200
