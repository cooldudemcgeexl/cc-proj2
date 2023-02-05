from sqlalchemy import Column, String, Uuid
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Uuid, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    first_name = Column(String(100))
    last_name = Column(String(100))

