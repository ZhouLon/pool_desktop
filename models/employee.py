from db import db

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=False)
    hire_date = db.Column(db.DateTime, nullable=False)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'), nullable=False)  # 商家ID

    def __repr__(self):
        return f"<Employee {self.name} working as {self.position}>"
