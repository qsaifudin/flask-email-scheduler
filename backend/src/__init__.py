# src/__init__.py
from flask import Flask
from .models import db
# from routes import route_app
# from .tasks import make_celery

import os

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///emails.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Specify the path to the instance folder inside the src folder
    # instance_path = os.path.join(app.root_path, 'instance')
    # app.instance_path = instance_path

    # Initialize database
    db.init_app(app)

    # Import routes and register them
    from .routes import route_app
    # Register routes
    app.register_blueprint(route_app)
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
