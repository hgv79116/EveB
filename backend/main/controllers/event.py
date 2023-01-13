# pay attention to g and session

from flask import Blueprint, session, g, request, make_response
from flask.json import jsonify
import functools

from .. import services
from .user import login_required

event_bp = Blueprint('event', __name__, url_prefix = '/event')     
    
@event_bp.route("/createEvent/")
@login_required
def create_event():
    params = request.get_json()
    
    msg, status = services.create_event(params)
    
    return make_response(
        jsonify({
            'msg': msg
        }), 
        status, 
    )

@event_bp.route("/deleteEvent/")
@login_required
def delete_event():     
    params = request.get_json()
    
    msg, status = services.delete_event(params)
    
    return make_response(
        jsonify({
            'msg': msg
        }), 
        status, 
    )

@event_bp.route("/loadEvent/")
@login_required
def load_event():     
    params = request.get_json()
    
    msg, status, event = services.load_event(params)
    
    return make_response(
        jsonify({
            'msg': msg, 
            'event': event,
        }), 
        status, 
    )
    
@event_bp.route("/updateEvent/")
@login_required
def update_event(): 
    params = request.get_json()
    
    msg, status, user = services.update_event(params)
    
    return make_response(
        jsonify({
            'msg': msg
        }), 
        status, 
    )
    
@event_bp.route("/parseEvent/")
@login_required
def parseEvent(): 
    params = request.get_json()
    
    msg, status, event = services.parse_event(params)
    
    return make_response(
        jsonify({
            'msg': msg, 
            'event': event, 
        }), 
        status, 
    )