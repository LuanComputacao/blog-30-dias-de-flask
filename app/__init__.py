from flask import Flask
from dynaconf import FlaskDynaconf
from app import views, models


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    FlaskDynaconf(app)
    views.init_app(app)
    models.init_app(app)

    return app
