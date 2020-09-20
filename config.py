class Config:
  '''
  general configuration class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'

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
