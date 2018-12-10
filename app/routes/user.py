from app import app, db
from app.models.User import User
# from app.decorators.check_bearerToken import token_required
from flask import json, jsonify, request, Response
from app.helpers.error_funcs import invalid_request_method, invalid_request_headers
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required


@app.route("/users", methods=['GET', 'POST'])
def users_Index():
  if request.method == 'GET':
    return get_all_users()
  elif request.method == 'POST':
    return register_user()
  else:
    return invalid_request_method()



@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def users_WithId(id):
  if request.method == 'GET':
    return get_user_byId(id)
  elif request.method == 'PATCH':
    return edit_user_byId(id)
  elif request.method == 'DELETE':
    return delete_user_byId(id)
  else:
    return invalid_request_method()


@jwt_required
def get_all_users():
  users = User.find()
  context = {
    "success" : True,
    "message" : "Fetch All Users",
    "data" : []
  }
  for user in users:
    context['data'].append(user.toDict_WithRelations())
  response = jsonify(context)
  return response, 200



@jwt_required
def register_user():
  header_content_type = request.headers.get("Content-Type")
  statusCode = 201
  context = {
    "success" : True,
    "message" : "Create New User",
    "data" : None
  }
  if header_content_type == 'application/json':
    user = User(email=request.json["email"], fullname=request.json["fullname"])
    user.set_password(request.json["password"])
  elif header_content_type =='application/x-www-form-urlencoded':
    user = User(email=request.form["email"], fullname=request.form["fullname"])
    user.set_password(request.form["password"])
  else:
    return invalid_request_headers()
    
  try :
    user.create()
    context["data"] = user.toDict_WithRelations()
  except SQLAlchemyError as e:
    context['success'] = False
    context['message'] = str(e.__dict__['orig'])
    statusCode = 500
  return jsonify(context), statusCode



@jwt_required
def get_user_byId(id):
  user = User.findById(id)
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Get User By ID",
    "data" : {}
  }
  if user is not None:
    context['data'] = user.toDict_WithRelations()
  else:
    context['success'] = False
    context['message'] = "User Doesn't Exist"
    statusCode = 404
  return jsonify(context), statusCode



@jwt_required
def edit_user_byId(id):
  user = User.findById(id)
  statusCode = 200
  header_content_type = request.headers.get("Content-Type")
  context = {
    "success" : True,
    "message" : "Update User By ID",
    "data" : None
  }
  if user is not None:
    if header_content_type == 'application/json':
      user.fullname = request.json['fullname']
    elif header_content_type =='application/x-www-form-urlencoded':
      user.fullname = request.form['fullname']
    else:
      return invalid_request_headers()
    user.update()
    user = User.findById(id)
    context['data'] = user.toDict_WithRelations()
  else:
    context['success'] = False
    context['message'] = "User Doesn't Exist"
    statusCode = 404
    
  return jsonify(context), statusCode



@jwt_required
def delete_user_byId(id):
  user = User.findById(id)
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Delete User By ID",
  }
  if user is not None:
    user.delete()
  else:
    context['success'] = False
    context['message'] = "User Doesn't Exist"
    statusCode = 404
  return jsonify(context), statusCode
