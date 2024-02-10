# src/__init__.py
from flask import Flask
from models import db
from routes import route_app
from celery import Celery
import os

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///emails.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Specify the path to the instance folder inside the src folder
    instance_path = os.path.join(app.root_path, 'instance')
    app.instance_path = instance_path
    
    # Celery configuration
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'  # Redis as message broker
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'  # Redis as result backend
    app.config['CELERY_TIMEZONE'] = 'Asia/Singapore'  # Set timezone
    
    # Initialize Celery
    celery = Celery(app.import_name)
    celery.conf.update(app.config)

    # Attach Celery instance to the Flask app
    app.celery = celery
    
    # Initialize database
    db.init_app(app)
    
    # Initialize Celery
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    # Register routes
    app.register_blueprint(route_app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
