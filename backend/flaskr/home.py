from flask import current_app, g, Blueprint
from . import auth

bp = Blueprint("home", __name__)
# @bp.route("/")
# @auth.login_required
# def index(): 
#     return "lfjsdljfdsg"
