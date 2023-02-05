from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from ..blueprints import auth, root
from ..models import *

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    app.register_blueprint(root)
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    return app