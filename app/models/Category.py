from app import db
from sqlalchemy.orm import joinedload

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)


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
    return Category.query.all()


  def findById(id):
    return Category.query.get(id)

  
  def toDict(self):
    selfDict = {}
    for column in self.__table__.columns:
      selfDict[column.name] = getattr(self, column.name)
    return selfDict