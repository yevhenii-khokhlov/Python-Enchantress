from flask_login import login_required, current_user
from flask import Blueprint, jsonify, render_template

# from . import db


main = Blueprint('main', __name__)


@main.route('/')
def index():
    # response = jsonify(
    #     {
    #         "status": "success"
    #     }
    # )
    # return response, 200
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    # response = jsonify(
    #     {
    #         "status": "success",
    #         "user_name": current_user.name
    #     }
    # )
    # return response, 200
    return render_template('profile.html', name=current_user.name)
