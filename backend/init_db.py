from src.models import db
from src import create_app

app = create_app()

with app.app_context():
    db.create_all()
