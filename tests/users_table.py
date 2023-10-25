from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

db_url = 'postgresql://JULY:1356@localhost/JULYdb'
engine = create_engine(db_url, echo=True)
Base = declarative_base()


class USERS(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String)
    email = Column(String)
    password = Column(String)
    roles = Column(JSON)
    mediumPictureUrl = Column(String)
    smallPictureUrl = Column(String)
    status = Column(String)
    rating = Column(JSON)
    online = Column(String)
    name = Column(String)
    location = Column(String)
    registration = Column(String)
    icq = Column(String)
    skype = Column(String)
    originalPictureUrl = Column(String)
    info = Column(JSON)
    settings = Column(JSON)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
