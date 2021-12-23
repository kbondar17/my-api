from my_app.server import create_app
from my_app.bd.models import db


db.create_all(app=create_app())


