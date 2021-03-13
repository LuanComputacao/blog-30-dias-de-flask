from flask import Flask
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    migrate = Migrate(app, db)
    from .postagens_model import Postagens
    from .perfil_model import Perfil
    migrate.init_app(app, db)
