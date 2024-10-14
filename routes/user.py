from flask import Blueprint, request, jsonify
from services.user_service import get_user, add_user, update_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/user/<int:id>', methods=['GET'])
def get_user_info(id):
    user = get_user(id)
    return jsonify(user)

@user_bp.route('/user', methods=['POST'])
def add_user_info():
    data = request.get_json()
    result = add_user(data)
    return jsonify(result)

@user_bp.route('/user/<int:id>', methods=['PUT'])
def update_user_info(id):
    data = request.get_json()
    result = update_user(id, data)
    return jsonify(result)
