import os
from dotenv import load_dotenv

load_dotenv()

POSTGRES_LOCAL_BASE = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))

class Config: 
    # base class for all configs
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False
    
class DevConfig(Config): 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #wh
    
class TestConfig(Config): 
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False #wh
    SQLALCHEMY_TRACK_MODIFICATIONS = False #wh

class DeployConfig(Config): 
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = POSTGRES_LOCAL_BASE
    
config_by_name = {
    'dev': DevConfig, 
    'test': TestConfig, 
    'deploy': DeployConfig, 
}

key = Config.SECRET_KEY
