from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
import logging
import sys

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)
mail = Mail()


def create_app(config_name):
  app = Flask(__name__)
  
  app.logger.addHandler(logging.StreamHandler(sys.stdout))
  app.logger.setLevel(logging.ERROR)
  
  #creating app configurations
  app.config.from_object(config_options[config_name])
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
  #initializing flask extensions
  db.init_app(app)
  login_manager.init_app(app)
  bootstrap = Bootstrap(app)
  mail.init_app(app)

  
  #Registering the blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  
  #Registering login blue print
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix='/authenticate')
  
  #Configure UploadSet
  configure_uploads(app,photos)
  
  return app