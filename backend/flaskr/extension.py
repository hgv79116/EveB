from flask import Blueprint, render_template
from .auth import login_required
bp = Blueprint("extension", __name__, url_prefix="/extension")

# bp.route must come before login_required. have not figured out why
@bp.route("/home") 
@login_required
def index(): 
    return render_template("extension/home.html")
