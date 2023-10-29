from sqlalchemy import Column, String, Boolean, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    UserId = Column(Integer, primary_key=True, autoincrement=True)
    Login = Column(String(100))
    Email = Column(String(100))
    Password = Column(String(100))
    Name = Column(String(100))
    Activated = Column(Boolean, nullable=False)
    Roles = Column(JSON)
    Status = Column(String(100))
