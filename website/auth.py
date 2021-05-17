from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    """
    Routes to the login page
    """
    return render_template('login.html')

@auth.route('/login', methods=['GET', 'POST'])
def login_post():
    """
    Checks user's credentials and logs them in
    """
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)

    return redirect(url_for('main.profile'))

@auth.route('/signup', methods=['POST'])
def signup_post():
    """
    Signs up the user and saved their details into the database.
    """
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.' , 'error')
        return redirect(url_for('auth.login'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    flash('Acount created. Login with your credentials.', 'success')
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    """
    Logouts out the user
    """
    logout_user()
    return redirect(url_for('main.home'))
