from flask import Blueprint, request, jsonify
from services.notification_service import get_notification, add_notification, update_notification

notification_bp = Blueprint('notification', __name__)

@notification_bp.route('/notification/<int:id>', methods=['GET'])
def get_notification_info(id):
    notification = get_notification(id)
    return jsonify(notification)

@notification_bp.route('/notification', methods=['POST'])
def add_notification_info():
    data = request.get_json()
    result = add_notification(data)
    return jsonify(result)

@notification_bp.route('/notification/<int:id>', methods=['PUT'])
def update_notification_info(id):
    data = request.get_json()
    result = update_notification(id, data)
    return jsonify(result)
