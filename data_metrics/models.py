# -*- coding: UTF-8 -*-
# from sqlalchemy import Column, Integer, String, Table
# from sqlalchemy.orm import mapper
# from data_metrics.database import metadata, db_session
from . import db


class Users(db.Model):
    # query = db_session.query_property()

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name


# users = Table('users', metadata,
#               Column('id', Integer, primary_key=True),
#               Column('name', String(50), unique=True),
#               Column('email', String(120), unique=True),
#               autoload=True
#               )
