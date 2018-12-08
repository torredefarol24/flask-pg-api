from app import db 

class Order_Product(db.Model):
  __tablename__ = 'order_product'
  id = db.Column(db.Integer, primary_key=True)
  order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)

  
