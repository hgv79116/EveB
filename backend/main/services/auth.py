from ..database import db
from ..models import User

def registerUser(params): 
    try: 
        new_user = User(**params)
        db.session.add(new_user)
        print("new user: ", new_user.email)
        db.session.commit()
        return "registerUser suceeded", 200
    except Exception as e:
        print("exception: ", e) 
        return "registerUser failed", 401

def validateUser(params): 
    assert params.get('username') or params.get('email'), "params wrong format"
    try: 
        user = None
        # print(params['username'])
        # print(params['password'])
        if params.get('username') is not None: 
            user = db.one_or_404(db.select(User).filter_by(username=params['username']))
            # print(user)
        else: 
            user = db.one_or_404(db.select(User).filter_by(email=params['useremail']))
            
        if user.password == params['password']: 
            return "validattion succeeded", 200, user
        
        return "wrong password", 401, None
    except:
        return "user not found", 401, None

def load_user_from_id(id): 
    user = db.one_or_404(db.select(User).filter_by(id=id))
    return user
    