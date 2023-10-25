from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, text, Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID

db_url = 'postgresql://JULY:1356@localhost/JULYdb'
engine = create_engine(db_url, echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'USERS2'

    UserId = Column(UUID, primary_key=True)
    Login = Column(String(100))
    Email = Column(String(100))
    Password = Column(String(100))
    Name = Column(String(100))
    Activated = Column(Boolean, nullable=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
