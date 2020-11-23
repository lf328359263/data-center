# -*- coding: UTF-8 -*-
from . import db


class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name


class EventCount(db.Model):

    __bind_key__ = 'ga'
    __tablename__ = 'ga_event_count'

    day = db.Column(db.DATE, primary_key=True)
    project_id = db.Column(db.String(10), primary_key=True)
    event_id = db.Column(db.String(255), primary_key=True)
    counts = db.Column(db.Integer)
    users = db.Column(db.Integer)
    avg_counts = db.Column(db.FLOAT)

    def __init__(self, day=None, project_id=None, event_id=None, counts=None, users=None, avg_counts=None):
        self.day = day
        self.project_id = project_id
        self.event_id = event_id
        self.counts = counts
        self.users = users
        self.avg_counts = avg_counts
