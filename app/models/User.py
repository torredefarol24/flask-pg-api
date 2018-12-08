from app import db, bcrypt

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fullname = db.Column(db.String(120))
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(), nullable=False)
  todos = db.relationship('Todo', backref='owner', lazy=True)
  # todos = db.relationship("Todo", lazy='select', backref=db.backref('owener, lazy='joined))   
  
  def __repr__(self):
    return f'<User {self.email}'
  
  def set_password(self, password):
    self.password = bcrypt.generate_password_hash(password)

  def check_password(self, password):
    return bcrypt.check_password_hash(self.password, password)
  
  def create(self):
    db.session.add(self)
    db.session.commit()
  
  def save(self):
    db.session.commit()
  
  def delete(self):
    db.session.delete()
    db.session.commit()
  
  def toDict(self):
    selfDict = {}
    for column in self.__table__.columns:
      selfDict[column.name] = getattr(self, column.name)
    return selfDict


