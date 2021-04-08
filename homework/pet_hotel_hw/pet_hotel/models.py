from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer)
    nickname = db.Column(db.String)
    room_number = db.Column(db.Integer)
    check_in_date = db.Column(db.Date)


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_id = db.Column(db.Integer)
    activity_type = db.Column(db.String)
    time = db.Column(db.Time)
