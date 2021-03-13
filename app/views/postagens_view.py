from flask import Blueprint

bp_postagens = Blueprint('postagens', __name__)


@bp_postagens.route('/', defaults={'id': None})
@bp_postagens.route('/<int:id>/')
def postagem(id: int):
    return {'status': 'Ok!'}
