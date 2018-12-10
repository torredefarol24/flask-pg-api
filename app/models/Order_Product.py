from app import db 

class Order_Product(db.Model):
  __tablename__ = 'order_product'
  id = db.Column(db.Integer, primary_key=True)
  order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'))


  # def __repr__(self):
  #   return f'Order_Product {self.id}'


  # def create(self):
  #   db.session.add(self)
  #   db.session.commit()


  # def toDict():
  #   selfDict = {}
  #   for column in self.__table__.columns:
  #     selfDict[column.name] = getattr(self, column.name)
  #   return selfDict


  # def toDict_WithRelations(self):
  #   selfDict_WithRel = {}

  #   for key in self.__mapper__.relationships.keys():
  #     relation_name = str(self.__mapper__.relationships[key])
  #     relation_items = getattr(self, key)
  #     is_list = self.__mapper__.relationships[key].uselist

  #     if is_list:
  #       selfDict_WithRel[relation_name] = []
  #       for item in relation_items:
  #         dictItem = item.toDict()
  #         selfDict_WithRel[relation_name].append(dictItem)
  #     else:
  #       selfDict_WithRel[relation_name] = relation_items.toDict()
      
  #   return selfDict_WithRel