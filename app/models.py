from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255))
  pass_secure = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True,index = True)
  pitch_id = db.relationship('Pitch',backref = 'user',lazy="dynamic")
  comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
  pass_secure  = db.Column(db.String(255))
                           
  @property
  def password(self):
      raise AttributeError('You cannot read the password attribute')
  @password.setter
  def password(self, password):
      self.pass_secure = generate_password_hash(password)
  def verify_password(self,password):
      return check_password_hash(self.pass_secure,password)
  def __repr__(self):
    return f'User {self.username}'
  
class Pitch(db.Model):
  __tablename__ = 'pitches'
  id = db.Column(db.Integer,primary_key = True)
  title = db.Column(db.String(255))
  pitch = db.Column(db.String(255))
  upvote = db.Column(db.Integer)
  downvote = db.Column(db.Integer)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  category = db.Column(db.String(100))
  comments = db.relationship('Comment',backref = 'user',lazy="dynamic")
  
  def save_pitch(self):
      db.session.add(self)
      db.session.commit() 
  
class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer,primary_key = True)
  comment = db.Column(db.String(255))
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  
  def save_comment(self):
      db.session.add(self)
      db.session.commit() 
  
  
