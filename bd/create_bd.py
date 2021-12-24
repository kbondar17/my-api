from my_app.app import create_app
from bd.models import db


db.create_all(app=create_app())


