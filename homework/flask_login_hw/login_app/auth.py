from flask_login import login_user, logout_user, login_required
from flask import Blueprint, redirect, url_for, request, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from .models import User
from . import db


auth = Blueprint('auth', __name__)


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

    email = data['email']
    name = data['name']
    password = data['password']

    # if this returns a user, then the email already exists in database
    user = User.query.filter_by(email=email).first()
    if user:     # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password, method='sha256')
    )

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['POST'])
def login_post():
    data = request.get_json()    # {"email": "y@com.ua", "password": "pass", "remember": "remember"}

    email = data['email']
    password = data['password']
    remember = True if data['remember'] else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))   # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))
