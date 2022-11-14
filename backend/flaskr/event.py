from flask import Blueprint, request, jsonify, g
from .auth import login_required
bp = Blueprint("event", __name__, url_prefix="/event")

@bp.route("/")
def home(): 
    return "hello!"

@bp.route("/parse", methods = ["POST"])
def parse(): 
    if g.user == None: 
        print ("failed")
        return jsonify({
            "status": "Login required"
        })
    else: 
        return jsonify({
            "status": "Success", 
            "event": {
                "name": "Event A", 
                "time": "11/12", 
                "location": "ABC"
            }
        })

@bp.route("/add")
@login_required
def add(): 
    pass

@bp.route("/delete")
@login_required
def delete(): 
    pass

@bp.route("/update")
def update(): 
    pass
