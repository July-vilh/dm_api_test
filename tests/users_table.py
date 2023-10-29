from sqlalchemy import create_engine, Column, String, Boolean, JSON, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from alembic import op
import sqlalchemy as sa

db_url = 'postgresql://JULY:1356@localhost/JULYdb'
engine = create_engine(db_url, echo=True)
Base = declarative_base()

def upgrade():
    op.alter_column('users', 'UserId', type_=sa.Integer, using="UserId::integer")


class USERS(Base):
    __tablename__ = 'users'

    UserId = Column(Integer, primary_key=True, autoincrement=True)
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
