from db import db

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchants.id'), nullable=False)  # 商家ID

    def __repr__(self):
        return f"<Notification {self.title}>"
