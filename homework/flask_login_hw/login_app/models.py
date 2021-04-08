from flask_login import UserMixin
from datetime import datetime

from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_time = db.Column(db.DateTime, default=datetime.utcnow)


class OrderLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100))
    price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
