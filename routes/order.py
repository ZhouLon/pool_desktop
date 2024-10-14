from flask import Blueprint, request, jsonify
from services.order_service import get_order, add_order, update_order

order_bp = Blueprint('order', __name__)

@order_bp.route('/order/<int:id>', methods=['GET'])
def get_order_info(id):
    order = get_order(id)
    return jsonify(order)

@order_bp.route('/order', methods=['POST'])
def add_order_info():
    data = request.get_json()
    result = add_order(data)
    return jsonify(result)

@order_bp.route('/order/<int:id>', methods=['PUT'])
def update_order_info(id):
    data = request.get_json()
    result = update_order(id, data)
    return jsonify(result)
