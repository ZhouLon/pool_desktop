from models.notification import Notification
from db import db

def get_notification(id):
    notification = Notification.query.get(id)
    if notification:
        return {
            "id": notification.id,
            "title": notification.title,
            "content": notification.content,
            "date_created": notification.date_created,
            "merchant_id": notification.merchant_id
        }
    return {"error": "Notification not found"}

def add_notification(data):
    new_notification = Notification(
        title=data['title'],
        content=data['content'],
        date_created=data['date_created'],
        merchant_id=data['merchant_id']
    )
    db.session.add(new_notification)
    db.session.commit()
    return {"message": "Notification added successfully"}

def update_notification(id, data):
    notification = Notification.query.get(id)
    if notification:
        notification.title = data.get('title', notification.title)
        notification.content = data.get('content', notification.content)
        db.session.commit()
        return {"message": "Notification updated successfully"}
    return {"error": "Notification not found"}
