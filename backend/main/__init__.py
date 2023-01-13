from .app import create_app
app = create_app('dev')

#debug 
from flask import session
from .models import User, Event
from .database import db
with app.app_context(): 
    johndoeinfo = { "username": "johndoe", "email": "johndoe@gmail.com" ,"password": "Random password"}
    johndoe = User(**johndoeinfo)
    user1 = User(username = 'giap', password = '10', email = 'giapvu2212@gmail.com')
    user2 = User(username = 'giap2', password =  '12', email = 'giapvu1222@gmail.com')
    db.drop_all()
    db.create_all()
    app.logger.info(user1.id)
    db.session.add(johndoe)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    app.logger.info(user2.password)
    # print(session.get('user_id'))