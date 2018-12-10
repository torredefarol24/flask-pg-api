from app import db

product_order_table = db.Table("product_order", 
  db.Column("id", db.Integer, primary_key=True),
  db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
  db.Column('order_id', db.Integer, db.ForeignKey('order.id'))
)
