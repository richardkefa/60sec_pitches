import os
class Config:
  '''
  general configuration class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  # simple mde  configurations

class ProdConfig(Config):
  '''
  production configuration child class
  '''
  pass

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production':ProdConfig 
}
