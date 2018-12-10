from app import db 

class Order_Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'))


  def __repr__(self):
    return f'Order_Product {self.id}'


  def create(self):
    db.session.add(self)
    db.session.commit()


  def toDict(self):
    selfDict = {}
    for column in self.__table__.columns:
      if column.name == 'id':
        continue
      selfDict[column.name] = getattr(self, column.name)

    return selfDict
