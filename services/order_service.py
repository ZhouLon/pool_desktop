from models.order import Order
from db import db

def get_order(id):
    order = Order.query.get(id)
    if order:
        return {
            "id": order.id,
            "merchant_id": order.merchant_id,
            "user_id": order.user_id,
            "product_name": order.product_name,
            "quantity": order.quantity,
            "total_price": order.total_price,
            "order_date": order.order_date
        }
    return {"error": "Order not found"}

def add_order(data):
    new_order = Order(
        merchant_id=data['merchant_id'],
        user_id=data['user_id'],
        product_name=data['product_name'],
        quantity=data['quantity'],
        total_price=data['total_price'],
        order_date=data['order_date']
    )
    db.session.add(new_order)
    db.session.commit()
    return {"message": "Order added successfully"}

def update_order(id, data):
    order = Order.query.get(id)
    if order:
        order.merchant_id = data.get('merchant_id', order.merchant_id)
        order.user_id = data.get('user_id', order.user_id)
        order.product_name = data.get('product_name', order.product_name)
        order.quantity = data.get('quantity', order.quantity)
        order.total_price = data.get('total_price', order.total_price)
        db.session.commit()
        return {"message": "Order updated successfully"}
    return {"error": "Order not found"}
