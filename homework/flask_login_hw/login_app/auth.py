from flask_login import login_user, logout_user, login_required
from flask import Blueprint, redirect, url_for, request, jsonify
from werkzeug.security import check_password_hash

from login_app.db_manager import DBManager


auth = Blueprint('auth', __name__)
db_manager = DBManager()


@auth.route('/login')
def login():
    response = jsonify(
        {
            "status": "success",
            "page_info": "this is login page"
        }
    )
    return response, 200


@auth.route('/signup')
def signup():
    response = jsonify(
        {
            "status": "success",
            "page_info": "this is signup page"
        }
    )
    return response, 200


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    response = jsonify(
        {
            "status": "success",
            "page_info": "logout user"
        }
    )
    return response, 200


@auth.route('/signup', methods=['POST'])
def signup_post():
    data = request.get_json()

    user = db_manager.sign_up(data)
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    data = request.get_json()    # {"email": "y@com.ua", "password": "pass", "remember": "remember"}

    user = db_manager.login(data)
    password = data.get("password")
    remember = data.get("remember")
    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))
