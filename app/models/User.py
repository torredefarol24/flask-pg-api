from app import db, bcrypt
from sqlalchemy.orm import joinedload

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fullname = db.Column(db.String(120))
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(), nullable=False)
  todos = db.relationship('Todo', backref='owner', lazy=True)
  orders = db.relationship("Order", backref='customer', lazy=True)

  
  def __repr__(self):
    return f'User {self.email}'
  

  def set_password(self, password):
    self.password = bcrypt.generate_password_hash(password).decode('utf-8')


  def check_password(self, password):
    return bcrypt.check_password_hash(self.password, password)
  

  def create(self):
    db.session.add(self)
    db.session.commit()
  

  def update(self):
    db.session.commit()
  

  def delete(self):
    db.session.delete()
    db.session.commit()


  def toDict(self):
    selfDict = {}
    for column in self.__table__.columns:
      if column.name == 'password':
        continue
      selfDict[column.name] = getattr(self, column.name)
    return selfDict


  def toDict_WithRelations(self):
    selfDict_WithRel = {}
    for column in self.__table__.columns:
      if column.name == 'password':
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
    

  def find():
    return User.query.options(joinedload(User.todos), joinedload(User.orders)).all()


  def findById(id):
    return User.query.options(joinedload(User.todos), joinedload(User.orders)).get(id)

  def findByEmail(emailVal):
    return User.query.filter_by(email=emailVal).first()
  


