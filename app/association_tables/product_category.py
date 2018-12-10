from app import db

product_category_table = db.Table("product_category", 
  db.Column("id", db.Integer, primary_key=True),
  db.Column('product_id', db.Integer, db.ForeignKey('product.id') ),
  db.Column('category_id', db.Integer, db.ForeignKey('category.id') ) 
)