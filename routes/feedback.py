from flask import Blueprint, request, jsonify
from services.feedback_service import get_feedback, add_feedback, update_feedback

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/feedback/<int:id>', methods=['GET'])
def get_feedback_info(id):
    feedback = get_feedback(id)
    return jsonify(feedback)

@feedback_bp.route('/feedback', methods=['POST'])
def add_feedback_info():
    data = request.get_json()
    result = add_feedback(data)
    return jsonify(result)

@feedback_bp.route('/feedback/<int:id>', methods=['PUT'])
def update_feedback_info(id):
    data = request.get_json()
    result = update_feedback(id, data)
    return jsonify(result)
