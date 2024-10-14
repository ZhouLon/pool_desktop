from models.employee import Employee
from db import db

def get_employee(id):
    employee = Employee.query.get(id)
    if employee:
        return {
            "id": employee.id,
            "name": employee.name,
            "position": employee.position,
            "salary": employee.salary,
            "hire_date": employee.hire_date,
            "merchant_id": employee.merchant_id
        }
    return {"error": "Employee not found"}

def add_employee(data):
    new_employee = Employee(
        name=data['name'],
        position=data['position'],
        salary=data['salary'],
        hire_date=data['hire_date'],
        merchant_id=data['merchant_id']
    )
    db.session.add(new_employee)
    db.session.commit()
    return {"message": "Employee added successfully"}

def update_employee(id, data):
    employee = Employee.query.get(id)
    if employee:
        employee.name = data.get('name', employee.name)
        employee.position = data.get('position', employee.position)
        employee.salary = data.get('salary', employee.salary)
        db.session.commit()
        return {"message": "Employee updated successfully"}
    return {"error": "Employee not found"}
