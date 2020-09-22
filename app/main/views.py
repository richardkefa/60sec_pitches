from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .forms import Pitchform,Commentform
from .. import db
import markdown2
from flask_login import login_required

@main.route('/')
def pitch():
  title = 'pitch in one minute'
  pitch=Pitch.query.all()
  if pitch is None:
      abort(404)
  # format_pitch = markdown2.markdown(pitch,extras=["code-friendly", "fenced-code-blocks"])
  return render_template('index.html',pitch = pitch,title = title)

@main.route('/comment/<int:id>')
def get_comment(id):
  comment = comment.query.filter_by()
  

@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def new_pitch():
  form = Pitchform()
  if form.validate_on_submit():
    title = form.title.data
    pitch = form.pitch.data
    category = form.category.data
    new_pitch = Pitch(title = title,pitch = pitch,category = category)
    new_pitch.save_pitch() 
    return redirect(url_for('main.pitch')) 
    
  return render_template('new_pitch_form.html',new_pitch = form)

@main.route('/comment/<int:post_id>',methods =['GET','POST'])
@login_required
def new_comment(post_id):
  form = Commentform()
  post = Post.query.get(post_id)
  all_comments = Comment.query.filter_by(post_id = pitch_id).all()
  
  if form.validate_on_submit():
    comment = form.title.data
    pitch_id = post_id
    user_id = current_user._get_current_object().id
    