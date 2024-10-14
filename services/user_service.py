from models.user import User
from db import db

def get_user(id):
    user = User.query.get(id)
    if user:
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    return {"error": "User not found"}

def add_user(data):
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=data['password']  # 密码通常需要加密存储
    )
    db.session.add(new_user)
    db.session.commit()
    return {"message": "User added successfully"}

def update_user(id, data):
    user = User.query.get(id)
    if user:
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)  # 需加密存储
        db.session.commit()
        return {"message": "User updated successfully"}
    return {"error": "User not found"}
