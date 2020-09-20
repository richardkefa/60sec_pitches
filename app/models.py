from . import db

class User(db.Model):
  __tablename_ = 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True,index = True)
  
  
  def __repr__(self):
    return f'User {self.username}'