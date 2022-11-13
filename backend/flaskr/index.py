from flask import current_app, g, Blueprint
from . import auth

bp = Blueprint("index", __name__)
@bp.route("/")
@auth.login_required
def index(): 
    return "lfjsdljfdsg"
