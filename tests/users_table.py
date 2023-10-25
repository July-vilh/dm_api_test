from sqlalchemy import create_engine, text, Column, String, Boolean, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

db_url = 'postgresql://JULY:1356@localhost/JULYdb'
engine = create_engine(db_url, echo=True)
Base = declarative_base()


class USERS(Base):
    __tablename__ = 'users'

    UserId = Column(UUID, primary_key=True)
    Login = Column(String(100))
    Email = Column(String(100))
    Password = Column(String(100))
    Name = Column(String(100))
    Activated = Column(Boolean, nullable=False)
    Roles = Column(JSON)
    Status = Column(String(100))


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
