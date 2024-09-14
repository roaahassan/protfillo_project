
from flask_login import UserMixin
from GuidedUpliftWebsit import db


class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(100))
    timetable = db.relationship('Timetable', backref='user')


class Timetable(db.Model, UserMixin):
    tbl_id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String())
    start_time = db.Column(db.Time())
    end_time = db.Column(db.Time())
    activity = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

