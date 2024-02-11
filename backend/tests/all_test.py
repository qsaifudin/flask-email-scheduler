import pytest
from flask import Flask, json
from src import create_app
from src.db.email import Email, db


@pytest.fixture
def app():
    app = create_app()
    app.config["TESTING"] = True
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_save_email(client, app):
    # Sample email data to be saved
    email_data = {
        "event_id": "1",
        "email_subject": "halo",
        "email_content": "ini halo",
        "timestamp": "11 Feb 2025 12:03",
    }

    # Make a POST request to save the email
    response = client.post("/save_emails", json=email_data)

    # Check if the response contains the expected data
    expected_data = {
        "data": {
            "event_id": "1",
            "email_subject": "halo",
            "email_content": "ini halo",
            "timestamp": "11 Feb 2025 12:03",
        },
        "status": "success",
        "message": "Email saved successfully",
    }
    
    assert response.json == expected_data

    # Check if the email has been saved to the database
    with app.app_context():
        saved_email = Email.query.filter_by(event_id=email_data["event_id"]).first()
        assert saved_email is not None
