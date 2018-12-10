from app import db
from datetime import datetime
from sqlalchemy.orm import joinedload
from app.models.Order_Product import Order_Product


class Order(db.Model):
  id = db.Column(db.Integer, primary_key = True) 
  created_at = db.Column(db.Date, default=datetime.now(), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  products = db.relationship(Order_Product, backref="order", primaryjoin = id == Order_Product.order_id)
  status = db.Column(db.String(120), default="Ordered", nullable=False)


  def __repr__(self):
    return f'Order {self.id}'
  

  def create(self):
    db.session.add(self)
    db.session.commit()

  
  def update(self):
    db.session.commit()
  

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  
  def find():
    return Order.query.options(joinedload(Order.products)).all()

  
  def findById(id):
    return Order.query.options(joinedload(Order.products)).get(id)

  
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
      else:
        selfDict_WithRel[relation_name] = relation_items.toDict()
      
    return selfDict_WithRel