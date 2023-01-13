from flask import Blueprint, session, g, request, make_response
from flask.json import jsonify
import functools

from .. import services

auth_bp = Blueprint('auth', __name__)

@auth_bp.before_app_request
def load_user(): 
    user_id = session.get('user_id')
    if user_id is None: 
        g['user_id'] = None
    else: 
        g['user_id'] = user_id
    
def login_required(endpoint):
    @functools.wraps(endpoint)
    def modified_endpoint(*args, **kwargs): 
        if g['user_id'] is None: 
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
        if g['user_id'] is not None: 
            g.clear()
            session.clear()
        return endpoint(*args, **kwargs)
        
    return modified_endpoint

@auth_bp.route("/registerUser/")
@logout_first
def registerUser(): 
    params = request.get_json()
    
    register_successful = services.registerUser(params)
    
    msg, status = "Successfully registered", 200 if register_successful else "Username or email already taken", 401
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
    
    validate_successful, user_id = services.validateUser(params)
    if validate_successful(): 
        assert isinstance(user_id, int), "user_id must be int, found {}".format(type(user_id))
        session.clear()
        session['user_id'] = user_id
    
    msg, status = "Successfully logged in", 200 if validate_successful else "Wrong credential", 401
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
