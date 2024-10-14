from flask import Blueprint, request, jsonify
from services.employee_service import get_employee, add_employee, update_employee

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/employee/<int:id>', methods=['GET'])
def get_employee_info(id):
    employee = get_employee(id)
    return jsonify(employee)

@employee_bp.route('/employee', methods=['POST'])
def add_employee_info():
    data = request.get_json()
    result = add_employee(data)
    return jsonify(result)

@employee_bp.route('/employee/<int:id>', methods=['PUT'])
def update_employee_info(id):
    data = request.get_json()
    result = update_employee(id, data)
    return jsonify(result)
