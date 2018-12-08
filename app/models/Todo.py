from app import db
from flask import json

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))

  def __repr__(self):
    return f'<Todo {self.title}>'

  def create(self):
    db.session.add(self)
    db.session.commit()

  def save(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def toDict(self):
    selfDict = {}
    for column in self.__table__.columns:
      selfDict[column.name] = getattr(self, column.name)
    return selfDict