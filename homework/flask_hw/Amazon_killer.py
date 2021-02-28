from dataclasses import dataclass
from flask import Flask, request
from datetime import datetime


amazon_killer = Flask(__name__)

USERS_DATABASE, CART_DATABASE = {}, {}
cart_counter, user_counter = 1, 1


@dataclass()
class NoSuchUser(Exception):
    user_id: int

    def __str__(self):
        return f'no user in base with id {self.user_id}'


@dataclass()
class NoSuchCart(Exception):
    cart_id: int

    def __str__(self):
        return f'no cart in base with id {self.cart_id}'


@amazon_killer.errorhandler(NoSuchUser)
def no_such_user_error_handler(error):
    return {"Error": str(error)}, 404


@amazon_killer.errorhandler(NoSuchCart)
def no_such_cart_handler(error):
    return {"Error": str(error)}, 404


@amazon_killer.route("/users", methods=["POST"])
def create_user():
    global user_counter
    user = request.json
    user['user_id'] = user_counter
    response = {
        "registration_timestamp": datetime.now().isoformat(),
        "user_id": user_counter
    }
    user["registration_timestamp"] = response["registration_timestamp"]
    USERS_DATABASE[user_counter] = user
    user_counter += 1
    return response, 201


@amazon_killer.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    try:
        user = USERS_DATABASE[user_id]
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return user


@amazon_killer.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = request.json
    response = {"status": "success"}
    try:
        USERS_DATABASE[user_id]["name"] = user["name"]
        USERS_DATABASE[user_id]["email"] = user["email"]
    except KeyError:
        raise NoSuchUser
    else:
        return response, 200


@amazon_killer.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global user_counter
    response = {"status": "success"}
    try:
        USERS_DATABASE[user_id].pop()
        user_counter -= 1
    except KeyError:
        raise NoSuchUser(user_id)
    else:
        return response, 200


@amazon_killer.route("/carts", methods=["POST"])
def create_cart():
    global cart_counter
    cart = request.json
    response = {
        "cart_id": cart_counter,
        "creating_time": datetime.now().isoformat()
    }
    cart["creating_time"] = response["creating_time"]
    cart["cart_id"] = cart_counter
    CART_DATABASE[cart_counter] = cart
    cart_counter += 1
    return response, 201


@amazon_killer.route("/carts/<int:cart_id>", methods=["GET"])
def get_cart(cart_id):
    try:
        cart = CART_DATABASE[cart_id]
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        return cart


@amazon_killer.route("/carts/<int:card_id>", methods=["PUT"])
def update_cart(cart_id):
    cart = request.json
    response = {"status": "success"}
    try:
        CART_DATABASE[cart_id]["products"] = cart["products"]
        CART_DATABASE[cart_id]["registration_time"] = cart["registration_time"]
    except KeyError:
        raise NoSuchCart(cart_id)
    else:
        return response, 200


@amazon_killer.route("/carts/<int:card_id>", methods=["DELETE"])
def delete_cart(cart_id):
    global cart_counter
    response = {"status": "success"}
    try:
        CART_DATABASE[cart_id].pop()
        cart_counter -= 1
    except KeyError:
        raise NoSuchCart
    else:
        return response, 200


if __name__ == "__main__":
    amazon_killer.run(debug=True)
    no_such_user_error_handler(NoSuchUser)
    no_such_cart_handler(NoSuchCart)
