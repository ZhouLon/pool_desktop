from models.merchant import Merchant
from db import db
def get_merchants(id):
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

def delete_merchant_by_id(merchant_id):
    merchant = Merchant.query.get(merchant_id)
    if merchant:
        db.session.delete(merchant)
        db.session.commit()
        return True
    return False

def search_merchants(merchant_id=None, name=None, address=None, phone=None):
    query = Merchant.query

    # 根据条件动态构建查询
    if merchant_id:
        query = query.filter(Merchant.id == merchant_id)
    if name:
        query = query.filter(Merchant.name.ilike(f"%{name}%"))
    if address:
        query = query.filter(Merchant.address.ilike(f"%{address}%"))
    if phone:
        query = query.filter(Merchant.phone.ilike(f"%{phone}%"))
    return query.all()  # 返回所有符合条件的商家
