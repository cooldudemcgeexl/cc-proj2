from flask import Blueprint, render_template

root = Blueprint('root', __name__)

@root.route('/')
def index():
    return render_template('index.html')

@root.route('/profile')
def profile():
    return render_template('profile.html')