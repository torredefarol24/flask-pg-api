from app import db
from sqlalchemy.orm import joinedload
from app.association_tables.product_category import product_category_table


class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  products = db.relationship("Product", secondary=product_category_table, back_populates="categories")

  def __repr__(self):
    return f'Category {self.name}'


  def create(self):
    db.session.add(self)
    db.session.commit()

  
  def update(self):
    db.session.commit()
  

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  
  def find():
    return Category.query.options(joinedload(Category.products)).all()


  def findById(id):
    return Category.query.options(joinedload(Category.products)).get(id)

  
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
