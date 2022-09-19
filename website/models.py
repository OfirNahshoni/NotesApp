from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    full_name = db.Column(db.String(100))
    notes = db.relationship('Note') # one User to many Notes
    # Profile attributes
    nickname = db.Column(db.String(50))
    phone_number = db.Column(db.String(50))
    state = db.Column(db.String(50))
    city = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    user_type = db.Column(db.String(50))
    profession = db.Column(db.String(50))
    addition_details = db.Column(db.String(200))
    img = db.Column(db.String(100), unique=True)
    img_filename = db.Column(db.String(500), unique=True)
    

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key
