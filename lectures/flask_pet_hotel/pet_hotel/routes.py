from flask import Blueprint, request
from pet_hotel.models import Owner


check_in_bp = Blueprint('chek-in', __name__, url_prefix='/check-in')
check_out_bp = Blueprint('chek-out', __name__, url_prefix='/check-out')


@check_in_bp.route('/', methods=['POST'])
@check_in_bp.route('', methods=['POST'])
def check_in():
    return 'success'


@check_in_bp.route('/owners')
def owners():
    return Owner.query.all()


@check_out_bp.route('/', methods=['POST'])
@check_out_bp.route('', methods=['POST'])
def check_out():
    return 'success'
