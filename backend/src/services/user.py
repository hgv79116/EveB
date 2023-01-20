# all db.model objects logics are implemented in services layer

from ..database import db
from ..models import User

DEFAULT_USER_INFO_KEYS = ['id', 'username', 'email']
FULL_USER_INFO_KEYS = ['id', 'username', 'email', 'phone', 'address', 'city', 'country', 'birthdate']

def extract_user_info(select_result, keys): 
    if select_result is None: 
        return None
    user_info = {}
    for key in keys: 
        user_info[key] = getattr(select_result, key)
    
    return user_info

def registerUser(params): 
    try: 
        new_user = User(**params)
        db.session.add(new_user)
        print("new user: ", new_user.email)
        db.session.commit()
        return "registerUser suceeded", 200
    except Exception as e:
        print("exception: ", e) 
        return "registerUser failed, exception: {}".format(e), 401

def deleteUser(params): 
    user = db.one_or_404(db.select(User).filter_by(id=params.get('id')))
    if params.get("password") != user.password: 
        return "Wrong password", 401
    try: 
        db.session.delete()
        db.session.commit()
        return "deleteUser suceeded", 200
    except Exception as e:
        return "deleteUser failed, exception: {}".format(e), 401
    
def validateUser(params): 
    assert params.get('username') or params.get('email'), "params wrong format: {}".format(params)
    print(params)
    try: 
        user = None
        if params.get('username') is not None: 
            user = db.one_or_404(db.select(User).filter_by(username=params['username']))
            # print(user)
        else: 
            user = db.one_or_404(db.select(User).filter_by(email=params['email']))
            
        if user.password == params['password']: 
            return "validattion succeeded", 200, extract_user_info(user, DEFAULT_USER_INFO_KEYS)
        
        return "wrong password", 401, None
    except Exception as e:
        print("not found")
        return "Exception: {}".format(e), 401, None

def load_user_from_id(id, load_full_info = False):
    keys = DEFAULT_USER_INFO_KEYS if not load_full_info else FULL_USER_INFO_KEYS
    try: 
        select_result = db.one_or_404(db.select(User).filter_by(id=id))
        return extract_user_info(select_result, keys)
    except Exception as e: 
        print(e)
        return None
    
    