from flask import Flask


def init_app(app: Flask):
    from .postagens_view import bp_postagens
    app.register_blueprint(bp_postagens)
