from . import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(100))


# class Timetable(db.Model):
#     table_id = db.Column(db.integer, primary_key=True, auto_increment=True)
#     day = db.Column(db.String())
#     time = db.Column(db.String())
#     subject = db.Column(db.String())
