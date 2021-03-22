from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user

from login_app.db_manager import DBManager


main = Blueprint('main', __name__)
db_manager = DBManager()


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

    orders = db_manager.get_orders(user_id)
    orders_lines = db_manager.get_order_lines(user_id)

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
    db_manager.orders_post(data=data, user_id=user_id)

    response = {
        "status": "success",
        "page_info": "order added",
    }
    return response, 201
