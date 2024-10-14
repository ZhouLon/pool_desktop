from flask import Blueprint, request, jsonify
from services.merchant_service import get_merchant, add_merchant, update_merchant

merchant_bp = Blueprint('merchant', __name__)

@merchant_bp.route('/merchant/<int:id>', methods=['GET'])
def get_merchant_info(id):
    merchant = get_merchant(id)
    return jsonify(merchant)

@merchant_bp.route('/merchant', methods=['POST'])
def add_merchant_info():
    data = request.get_json()
    result = add_merchant(data)
    return jsonify(result)

@merchant_bp.route('/merchant/<int:id>', methods=['PUT'])
def update_merchant_info(id):
    data = request.get_json()
    result = update_merchant(id, data)
    return jsonify(result)
