# src/__init__.py
from flask import Flask
from flask_cors import CORS
from .db.email import db
from .routes.emailRoute import route_app
from .config.db import DevelopmentConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config_class)
    
    CORS(app)

    # Initialize database
    db.init_app(app)
    
    # Register routes
    app.register_blueprint(route_app)
    
    return app

app = create_app()

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
