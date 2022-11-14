from flask import Blueprint, render_template, g, url_for, redirect, jsonify
from .auth import login_required
bp = Blueprint("extension", __name__, url_prefix="/extension")

@bp.route("/load_user") 
def load_user(): 
    if g.user is None: 
        return jsonify({"logged": 0, "login_link": url_for("auth.login", _external=True)}); 
    else: 
        return jsonify({"logged": 1, "username": g.username})
