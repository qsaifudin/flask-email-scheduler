# src/routes.py
from flask import request, Blueprint
from ..services.email_crud import save_email, get_all_emails,get_all_archived__emails, toggle_email_scheduler
from ..services.email_scheduler import get_scheduler_status

route_app = Blueprint("route_app", __name__)

@route_app.route("/save_emails", methods=["POST"])
def save_emails_route():
    data = request.json
    return save_email(data)

@route_app.route("/emails/all", methods=["GET"])
def get_all_emails_route():
    return get_all_emails()

@route_app.route("/archived_emails/all", methods=["GET"])
def get_all_archived_emails_route():
    return get_all_archived__emails()

@route_app.route("/toggle_email_scheduler", methods=["POST"])
def toggle_email_scheduler_route():
    enabled = request.args.get("enabled", "").lower() in ["true", "1", "on", "yes"]
    return toggle_email_scheduler(enabled)

@route_app.route("/scheduler/status", methods=["GET"])
def get_scheduler_status_route():
    return get_scheduler_status()