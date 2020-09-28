import os
class Config:
  '''
  general configuration class
  '''
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitching'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST ='app/static/photos'
  
  #  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
  '''
  production configuration child class
  '''
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
  DEBUG = False
  

class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitching_test'
  DEBUG = True

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}
