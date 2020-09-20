from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLALchemy

db = SQLALchemy

def create_app(config_name):
  app = Flask(__name__)
  
  #creating app configurations
  app.config.from_object(config_options[config_name])