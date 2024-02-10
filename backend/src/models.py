# src/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Email(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, nullable=False, primary_key=True)
    email_subject = db.Column(db.String(255), nullable=False)
    email_content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
