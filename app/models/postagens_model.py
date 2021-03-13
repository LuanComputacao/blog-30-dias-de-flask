from . import db


class Postagens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), unique=True, nullable=False)
    texto = db.Column(db.String, unique=False, nullable=False)
