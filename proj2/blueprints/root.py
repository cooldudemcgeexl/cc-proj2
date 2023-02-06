from flask import Blueprint, render_template
from flask_login import current_user, login_required

root = Blueprint('root', __name__)

@root.route('/')
@login_required
def index():
    return render_template('index.html')

@root.route('/profile')
@login_required
def profile():
    return render_template('profile.html',first_name = current_user.first_name, last_name = current_user.last_name, email=current_user.email)