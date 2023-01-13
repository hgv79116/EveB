import os
from flask import Flask
def create_app(test_config=None): 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE = os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    if test_config is None: 
        app.config.from_pyfile('config.py', silent=True)
    else: 
        app.config.from_mapping(test_config)

    try: 
        os.makedirs(app.instance_path)
    except OSError: 
        pass
    
    from .app.main import db
    db.init_app(app)
    
    from .app.main import auth
    app.register_blueprint(auth.bp) 
    
    from .app.main import extension
    app.register_blueprint(extension.bp)
    
    from .app.main import event
    app.register_blueprint(event.bp)
    
    return app

    