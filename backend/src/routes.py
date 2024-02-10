# src/routes.py
# from .main import app
from flask import request, jsonify, Blueprint
from models import db, Email
from datetime import datetime
import pytz

route_app = Blueprint("route_app", __name__)


@route_app.route("/save_emails", methods=["POST"])
def save_emails():
    data = request.json
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


@route_app.route("/emails/all", methods=["GET"])
def get_all_emails():
    emails = Email.query.all()
    email_data = [
        {
            # "id": email.id,
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


@route_app.route("/emails", methods=["GET"])
def get_emails():
    timestamp_str = request.args.get("timestamp")

    if not timestamp_str:
        return jsonify({"error": "Missing timestamp parameter"}), 400

    try:
        timestamp = datetime.strptime(timestamp_str, "%d %b %Y %H:%M")
        timestamp = pytz.timezone("Asia/Singapore").localize(timestamp)
    except ValueError:
        return jsonify({"error": "Invalid timestamp format"}), 400

    emails = Email.query.filter(Email.timestamp > timestamp).all()
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
        "message": "Retrieved emails after specified timestamp successfully",
        "data": email_data,
    }
    return jsonify(response), 200
