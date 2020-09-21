from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment,Category
from .. import db

@main.route('/')
def index():
  title = 'pitch in one minute'
  
  pitches = Pitch.query.all()
  
  return render_template('index.html', pitches = pitches, title = title)
@main.route('/comment/<int:id>')
def get_comment(id):
  comment = comment.query.filter_by()