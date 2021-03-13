from . import db


class Perfil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    bio = db.Column(db.String, unique=False, nullable=True)
