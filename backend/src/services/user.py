# all db.model objects logics are implemented in services layer

from ..database import db
from ..models import User

def remove_senstive(user): 
    if user is None: 
        return None
    return  { 
        'id': user.id, 
        'username': user.username, 
        'email': user.email, 
    }

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
            return "validattion succeeded", 200, remove_senstive(user)
        
        return "wrong password", 401, None
    except Exception as e:
        print("not found")
        return "Exception: {}".format(e), 401, None

def load_user_from_id(id): 
    user = db.one_or_404(db.select(User).filter_by(id=id))
    return remove_senstive(user)
    
    