from models.feedback import Feedback
from db import db

def get_feedback(id):
    feedback = Feedback.query.get(id)
    if feedback:
        return {
            "id": feedback.id,
            "user_id": feedback.user_id,
            "merchant_id": feedback.merchant_id,
            "content": feedback.content,
            "date_created": feedback.date_created
        }
    return {"error": "Feedback not found"}

def add_feedback(data):
    new_feedback = Feedback(
        user_id=data['user_id'],
        merchant_id=data['merchant_id'],
        content=data['content'],
        date_created=data['date_created']
    )
    db.session.add(new_feedback)
    db.session.commit()
    return {"message": "Feedback added successfully"}

def update_feedback(id, data):
    feedback = Feedback.query.get(id)
    if feedback:
        feedback.content = data.get('content', feedback.content)
        db.session.commit()
        return {"message": "Feedback updated successfully"}
    return {"error": "Feedback not found"}
