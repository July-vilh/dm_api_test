import records
from sqlalchemy import create_engine, text, Column, String, Boolean, select
import structlog
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID

from orm_client.orm_client import OrmClient

Base = declarative_base()

from generic.helpers.dm_db import dmDB

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


class User(Base):
    __tablename__ = 'USERS2'

    UserId = Column(UUID, primary_key=True)
    Login = Column(String(100))
    Email = Column(String(100))
    Password = Column(String(100))
    Name = Column(String(100))
    Activated = Column(Boolean, nullable=False)


def test_orm():
    POSTGRES_USER = 'JULY'
    POSTGRES_PASSWORD = '1356'
    host = 'localhost'
    POSTGRES_DB = 'JULYdb'
    # connection_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{host}/{POSTGRES_DB}"
    # isolation_level = 'AUTOCOMMIT'
    # db = create_engine(connection_string, isolation_level=isolation_level)
    # connect = db.connect()
    orm = OrmClient(POSTGRES_USER=POSTGRES_USER, POSTGRES_PASSWORD=POSTGRES_PASSWORD, host=host, POSTGRES_DB=POSTGRES_DB)
    query = select([User])
    dataset = orm.send_query(query)
