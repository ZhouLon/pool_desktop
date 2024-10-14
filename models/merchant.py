from db import db

class Merchant(db.Model):
    __tablename__ = 'merchants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    advertisement = db.Column(db.String(500))  # 广告信息
    feedback = db.relationship('Feedback', backref='merchant', lazy=True)
    orders = db.relationship('Order', backref='merchant', lazy=True)

    def __repr__(self):
        return f"<Merchant {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "advertisement": self.advertisement
        }