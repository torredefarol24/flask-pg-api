from app import db

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


  def __repr__(self):
    return f'<Todo {self.title}>'


  def create(self):
    db.session.add(self)
    db.session.commit()


  def update(self):
    db.session.commit()


  def delete(self):
    db.session.delete(self)
    db.session.commit()
  

  def toDict(self):
    selfDict = {}
    for column in self.__table__.columns:
      if column.name == 'user_id': 
        continue
      selfDict[column.name] = getattr(self, column.name)
    return selfDict

  
  def toDict_WithRelations(self):
    selfDict_WithRel = {}
    for column in self.__table__.columns:
      if column.name == 'user_id': 
        continue
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
