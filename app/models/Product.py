from app import db
from sqlalchemy.orm import joinedload
from app.association_tables.product_category import product_category_table
from app.association_tables.product_order import product_order_table


class Product(db.Model):
  id = db.Column(db.Integer, primary_key = True) 
  name = db.Column(db.String(120), nullable=False)
  details = db.Column(db.String(360))
  categories = db.relationship("Category", secondary=product_category_table, back_populates="products")
  orders = db.relationship("Order", secondary=product_order_table, back_populates="products")

  
  def __repr__(self):
    return f'Product {self.name}'
  

  def create(self):
    db.session.add(self)
    db.session.commit()

  
  def update(self):
    db.session.commit()
  

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  
  def find():
    return Product.query.options(joinedload(Product.orders), joinedload(Product.categories)).all()

  
  def findById(id):
    return Product.query.options(joinedload(Product.orders), joinedload(Product.categories)).get(id)


  def toDict(self):
    selfDict = {}
    for column in self.__table__.columns:
      selfDict[column.name] = getattr(self, column.name)
    return selfDict

  
  def toDict_WithRelations(self):
    selfDict_WithRel = {}
    for column in self.__table__.columns:
      selfDict_WithRel[column.name] = getattr(self, column.name)

    for key in self.__mapper__.relationships.keys():
      relation_name = str(self.__mapper__.relationships[key])
      relation_items = getattr(self, key)
      is_list = self.__mapper__.relationships[key].uselist

      if is_list:
        selfDict_WithRel[relation_name] = []
        for item in relation_items:
          dictItem = item.toDict()
          selfDict_WithRel[relation_name].append(dictItem)
      else :
        selfDict_WithRel[relation_name] = relation_items.toDict()

    return selfDict_WithRel
