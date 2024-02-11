# src/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Email(db.Model):
    event_id = db.Column(db.Integer, nullable=False, primary_key=True)
    email_subject = db.Column(db.String(255), nullable=False)
    email_content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class ArchiveEmail(db.Model):
    event_id = db.Column(db.Integer, nullable=False, primary_key=True)
    email_subject = db.Column(db.String(255), nullable=False)
    email_content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
