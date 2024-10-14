from models.merchant import Merchant
from db import db

def get_merchant(id):
    merchant = Merchant.query.get(id)
    if merchant:
        return {
            "id": merchant.id,
            "name": merchant.name,
            "address": merchant.address,
            "phone": merchant.phone,
            "advertisement": merchant.advertisement
        }
    return {"error": "Merchant not found"}

def add_merchant(data):
    new_merchant = Merchant(
        name=data['name'],
        address=data['address'],
        phone=data['phone'],
        advertisement=data.get('advertisement', '')
    )
    db.session.add(new_merchant)
    db.session.commit()
    return {"message": "Merchant added successfully"}

def update_merchant(id, data):
    merchant = Merchant.query.get(id)
    if merchant:
        merchant.name = data.get('name', merchant.name)
        merchant.address = data.get('address', merchant.address)
        merchant.phone = data.get('phone', merchant.phone)
        merchant.advertisement = data.get('advertisement', merchant.advertisement)
        db.session.commit()
        return {"message": "Merchant updated successfully"}
    return {"error": "Merchant not found"}
