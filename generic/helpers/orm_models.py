# from sqlalchemy import Column, String, Boolean, Integer, JSON
# from sqlalchemy.ext.declarative import declarative_base
# metadata = MetaData()
#
#
#
# Base = declarative_base()


# coding: utf-8
from sqlalchemy import Boolean, Column, JSON, MetaData, String, Table
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()


t_users = Table(
    'users', metadata,
    Column('UserId', UUID),
    Column('Login', String(100)),
    Column('Email', String(100)),
    Column('Password', String(100)),
    Column('Name', String(100)),
    Column('Activated', Boolean),
    Column('Roles', JSON),
    Column('Status', String(100))
)


