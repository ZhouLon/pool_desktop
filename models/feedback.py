from db import db

class Feedback(db.Model):
    __tablename__ = 'feedbacks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # 用户ID
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'), nullable=False)  # 商家ID
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Feedback from user {self.user_id} to merchant {self.merchant_id}>"
