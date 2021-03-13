from flask import Blueprint

account_bp = Blueprint('accounts', __name__, url_prefix="/accounts")


@account_bp.route('/')
def list_accounts():
    return {}
