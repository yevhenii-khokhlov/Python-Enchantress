from flask_login import login_required, current_user
from flask import Blueprint, jsonify, request
from datetime import datetime

from .models import Orders, OrderLine
from . import db


main = Blueprint('main', __name__)


@main.route('/')
def index():
    response = jsonify(
        {
            "status": "success",
            "page_info": "start page",
        }
    )
    return response, 200


@main.route('/profile')
@login_required
def profile():
    response = jsonify(
        {
            "status": "success",
            "page_info": "profile page",
            "user_name": current_user.name,
            "user_id": current_user.id,
        }
    )
    return response, 200


@main.route('/orders')
@login_required
def order_list():
    user_id = current_user.get_id()

    orders = Orders.query.filter_by(user_id=user_id).all()
    orders_lines = OrderLine.query.filter_by(user_id=user_id).all()

    orders_for_return, orders_lines_for_return = {}, {}
    if orders:
        for order in orders:
            orders_for_return[f"order_{order.id}"] = {
                "user_id": order.user_id,
                "order_time": order.order_time,
            }
    if orders_lines:
        for line in orders_lines:
            orders_lines_for_return[f"order_line_{line.id}"] = {
                "product": line.product,
                "price": line.price,
            }
    response = {
        "status": "success",
        "page_info": "orders page",
        "orders": orders_for_return,
        "orders_lines": orders_lines_for_return,
    }
    return response, 200


@main.route('/orders', methods=['POST'])
@login_required
def order_post():
    user_id = current_user.get_id()
    data = request.get_json()

    order = Orders(
        order_time=datetime.utcnow(),
        user_id=user_id,
    )
    order_line = OrderLine(
        product=data["product"],
        price=data["price"],
        user_id=user_id,
    )
    db.session.add(order)
    db.session.add(order_line)
    db.session.commit()

    response = {
        "status": "success",
        "page_info": "order added",
    }
    return response, 201
