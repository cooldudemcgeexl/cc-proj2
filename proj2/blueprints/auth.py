from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from ..app.database import db
from ..models import User

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


...


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user: User = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Login failed. Check your password and try again.')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember)
    return redirect(url_for('root.profile'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, first_name=first_name, last_name=last_name,
                    password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return 'Logout'
