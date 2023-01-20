# pay attention to g and session
# session is stored in cache, so it must not contain any sensitive information
# on the other hand g is safe? 

from flask import Blueprint, session, g, request, make_response
from flask.json import jsonify
import functools

from .. import services

user_bp = Blueprint('user', __name__, url_prefix = '/user')

def end_session(): 
    g.user = None
    session.clear()

def start_session(user): 
    session['user_id'] = user['id']

@user_bp.before_app_request # applied for all blue print
def load_user(): 
    print("loading user")
    user_id = session.get('user_id')
    if user_id: 
        g.user = services.load_user_from_id(user_id)
    else: 
        g.user = None
    
def login_required(endpoint):
    @functools.wraps(endpoint)
    def modified_endpoint(*args, **kwargs): 
        print("checking logged in")
        if g.user is None: 
            print("Not logged in")
            return make_response(
                jsonify({ 
                    'msg': "Not logged in", 
                }), 
                401
            )
        return endpoint(*args, **kwargs)
        
    return modified_endpoint
    
@user_bp.route("/login/", methods = ["POST"])
def login():
    params = request.get_json()
    
    msg, status, user = services.validateUser(params)
    
    if user is not None: 
        end_session()
        start_session(user)
        
    return make_response(
        jsonify({ 
            'msg': msg, 
            'user': user
        }), 
        status, 
    )

@user_bp.route("/logout/")
@login_required
def logout(): 
    end_session()    
    
    return make_response(
        jsonify({
            'msg': "Successfully logged out", 
        }), 
        200
    )

@user_bp.route("/registerUser/", methods = ["POST"])
def registerUser(): 
    print("registering")
    params = request.get_json()
    
    msg, status = services.registerUser(params)
    
    return make_response(
        jsonify({ 
            'msg': msg 
        }), 
        status, 
    )

@user_bp.route("/deleteUser/", methods = ["POST"])
@login_required
def deleteUser():     
    params = request.get_json()
    params.id = session["user_id"]
    
    msg, status = services.deleteUser(params)
    if status == 200: 
        end_session()
        
    return make_response(
        jsonify({ 
            'msg': msg 
        }), 
        status, 
    )
    
@user_bp.route("/loadUser/")
def loadUser():
    user_id = session.get('user_id') 
    msg = "Logged in" if user_id else "Not logged in"
    user = services.load_user_from_id(user_id) if user_id else None
    
    print(msg)
    
    return make_response(
        jsonify({
            'msg': msg, 
            'user': user
        }), 
        200, 
    )
    
@user_bp.route("/getInfo/")
@login_required
def getFullInfo(): 
    user_id = session.get('user_id') 
    print(user_id)
    if user_id is None: 
        return make_response(
        jsonify({
            'msg': "Not logged in", 
        }), 
        401, 
    )
    else: 
        user = services.load_user_from_id(user_id, load_full_info=True) 
        
        return make_response(
            jsonify({
                'msg': "Succeeded", 
                'user': user
            }), 
            200, 
        )