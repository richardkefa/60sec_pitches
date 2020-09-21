from . import db

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255),unique = True,index = True)
  pitch_id = db.relationship('Pitch',backref = 'user',lazy="dynamic")
  
  def __repr__(self):
    return f'User {self.username}'
  
class Pitch(db.Model):
  __tablename__ = 'pitches'
  id = db.Column(db.Integer,primary_key = True)
  pitch = db.Column(db.String(255))
  upvote = db.Column(db.Integer)
  downvote = db.Column(db.Integer)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  category = db.Column(db.String(100))
  comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
  
  
class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer,primary_key = True)
  comment = db.Column(db.String(255))
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
  
  
