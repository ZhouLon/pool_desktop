from flask import Blueprint, request, jsonify
from services.merchant_service import search_merchants, add_merchant, update_merchant,delete_merchant_by_id,get_merchants

merchant_bp = Blueprint('merchant', __name__)

@merchant_bp.route('/merchant/search', methods=['GET'])
def search_merchant():
    merchant_id = request.args.get('id')
    name = request.args.get('name')
    address = request.args.get('address')
    phone = request.args.get('phone')
    # 调用服务层函数查询商家
    merchants = search_merchants(merchant_id=merchant_id, name=name, address=address, phone=phone)
    if merchants:
        return jsonify([merchant.to_dict() for merchant in merchants])  # 返回JSON
    else:
        return jsonify({"error": "No merchant found"}), 404

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
@merchant_bp.route('/merchant/<int:merchant_id>', methods=['GET'])
def get_merchant(merchant_id):
    merchant = search_merchants(merchant_id)
    print(merchant)
    if merchant:
        print(merchant[0].to_dict())
        return jsonify(merchant[0].to_dict())
    else:
        return jsonify({"error": "Merchant not found"})

@merchant_bp.route('/merchant/<int:merchant_id>', methods=['DELETE'])
def delete_merchant(merchant_id):
    result = delete_merchant_by_id(merchant_id)
    if result:
        return jsonify({"message": f"Merchant with id {merchant_id} deleted successfully"})
    else:
        return jsonify({"error": "Merchant not found"})
