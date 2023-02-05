from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

from ..app.database import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))

