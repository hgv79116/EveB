# The way flask alchemy is structured is quite weird and does not work well naturally with blueprint. Some solutions: 
# 1. When initializing apps an instance of class Services which has the knowledge of the db and models will be created and attached to the app. controllers and services will communicate via app proxies
# 2. This problem boils down to sharing resources between modules. Basically the resource need is circular, which can be solved if we just put everything into one file. 
# An alternative to this is to 
# 3. create db.py. Imports: app.py <- blueprints (controllers), app <- db, blueprints <- services, services <- models, services <- db, models <- db

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from .config import config_by_name

from .controllers import *
from .database import db

flask_bcrypt = Bcrypt()

def create_app(config_name): 
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
    flask_bcrypt.init_app(app)

    app.register_blueprint(event_bp)
    app.register_blueprint(user_bp)
    CORS(app)
    
    return app

app = create_app('dev')