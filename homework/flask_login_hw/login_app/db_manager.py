from datetime import datetime
from werkzeug.security import generate_password_hash

from . import db
from login_app.models import User, Orders, OrderLine


class DBManager:
    @staticmethod
    def load_user(user_id: int):
        user = User.query.get(user_id)
        return user

    @staticmethod
    def sign_up(data: dict):
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            new_user = User(
                email=email,
                name=name,
                password=generate_password_hash(password, method='sha256')
            )

            db.session.add(new_user)
            db.session.commit()
        return user

    @staticmethod
    def login(data: dict):
        email = data.get('email')
        user = User.query.filter_by(email=email).first()
        return user

    @staticmethod
    def get_orders(user_id: int):
        orders = Orders.query.filter_by(user_id=user_id).all()
        return orders

    @staticmethod
    def get_order_lines(user_id: int):
        orders_lines = OrderLine.query.filter_by(user_id=user_id).all()
        return orders_lines

    @staticmethod
    def orders_post(data: dict, user_id: int):
        order = Orders(
            order_time=datetime.utcnow(),
            user_id=user_id,
        )
        order_line = OrderLine(
            product=data.get("product"),
            price=data.get("price"),
            user_id=user_id,
        )
        db.session.add(order)
        db.session.add(order_line)
        db.session.commit()
