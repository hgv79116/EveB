# pay attention to g and session

from flask import Blueprint, session, g, request, make_response
from flask.json import jsonify
import functools

from .. import services

auth_bp = Blueprint('auth', __name__, url_prefix = '/auth')

@auth_bp.before_app_request
def load_user(): 
    user_id = session.get('user_id')
    if user_id is None: 
        g.user = None
    else: 
        g.user = services.load_user_from_id(user_id)
    
def login_required(endpoint):
    @functools.wraps(endpoint)
    def modified_endpoint(*args, **kwargs): 
        if g.user is None: 
            msg, status = "Not logged in", 401
            return make_response(
                jsonify({ 
                    'msg': msg, 
                }), 
                status
            )
        return endpoint(*args, **kwargs)
        
    return modified_endpoint
        

def logout_first(endpoint):
    @functools.wraps(endpoint)
    def modified_endpoint(*args, **kwargs): 
        if g.user is not None: 
            g.user = None
            session.clear()
        return endpoint(*args, **kwargs)
        
    return modified_endpoint

@auth_bp.route("/registerUser/")
@logout_first
def registerUser(): 
    params = request.get_json()
    
    msg, status = services.registerUser(params)
    
    return make_response(
        jsonify({ 
            'msg': msg 
        }), 
        status, 
    )
    
@auth_bp.route("/login/")
@logout_first
def login():
    params = request.get_json()
    
    msg, status, user = services.validateUser(params)
    
    if user is not None: 
        session.clear()
        session['user_id'] = user.id
    
    return make_response(
        jsonify({
            'msg': msg
        }), 
        status, 
    )

@auth_bp.route("/logout/")
@login_required
def logout(): 
    
    session.clear()
    
    msg, status = "Successfully logged out", 200
    return make_response(
        jsonify({
            'msg': msg, 
        }), 
        status
    )