from flask import render_template,redirect,url_for,flash,request
from ..models import User
from flask_login import login_user,logout_user,login_required
from .forms import RegistrationForm,LoginForm
from .. import db
from . import auth

@auth.route('/login',methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
      user = User.query.filter_by(username = form.username.data).first()
      if user is not None and user.verify_password(form.password.data):
          login_user(user,form.remember.data)
          return redirect(request.args.get('next') or url_for('main.pitch'))
      flash('Invalid username or Password')

  return render_template('auth/login.html',form = form)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form = form)
  
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.pitch"))
