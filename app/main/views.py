from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .forms import Pitchform,Commentform,Profileform
from .. import db,photos
from flask_login import login_required,current_user

@main.route('/')
def pitch():
  title = 'pitch in one minute'
  pitches=Pitch.query.all()
  if pitches is None:
      abort(404)
  # print(pickup_line)
  # import pdb; pdb.set_trace()
  return render_template('index.html',pitches = pitches,title = title)
@main.route('/pickup')
def pickup_line():
  pickup_line=Pitch.query.filter_by(category = '2').all()
  
  return render_template('categories/pick_up_line.html',pickup_line=pickup_line)
  
@main.route('/product')
def product_pitch():
  product_pitch=Pitch.query.filter_by(category = '3').all()
  print(product_pitch)
    
  return render_template('categories/product_pitch.html',product_pitch=product_pitch)
  
@main.route('/investor')
def investor_pitch():
  investor_pitch=Pitch.query.filter_by(category = '1').all()
    
  return render_template('categories/investor_pitch.html',investor_pitch=investor_pitch)

  
@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def new_pitch():
  form = Pitchform()
  if form.validate_on_submit():
    pitch_title = form.title.data
    pitch = form.pitch.data
    category = form.category.data
    new_pitch = Pitch(pitch_title = pitch_title,pitch = pitch,category = category)
    new_pitch.save_pitch() 
    return redirect(url_for('main.pitch')) 
    
  return render_template('new_pitch_form.html',new_pitch = form)

@main.route('/comment/<int:pitch_id>',methods =['GET','POST'])
# @login_required
def new_comment(pitch_id):
  form = Commentform()
  # pitch = Pitch.query.get(pitch_id)
  all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
  
  if form.validate_on_submit():
    comment = form.comment.data
    pitch_id = pitch_id
    # user_id = current_user._get_current_object().id
    new_comment =Comment(comment = comment,pitch_id = pitch_id)
    new_comment.save_comment()
    return redirect(url_for('main.new_comment',pitch_id = pitch_id))
  # print(all_comments)
  return render_template('comments/comments.html', form = form,all_comments = all_comments)


@main.route('/profile/<username>',methods =['GET','POST'])
def update_profile(username):
  user = User.query.filter_by(username = username).first()
  form = Profileform()
  if form.validate_on_submit():
    user.bio = form.bio.data
    db.session.add(user)
    db.session.commit()   
    return redirect(url_for('.profile'), username = username)
  return render_template('main.profile',form = form) 

@main.route('/<username>/profile')
def profile(username):
    user = User.query.filter_by(username = username).first()
    bio = user.bio
    user_id = current_user._get_current_object().id
    profile_posts = Pitch.query.filter_by(user_id = user_id).all()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user,bio = bio, profile_posts=profile_posts)
  
@main.route('/user/<username>/update/pic',methods= ['POST'])
# @login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.photo_path = path
        db.session.commit()
    return redirect(url_for('main.profile',username=username))
  
  

    
