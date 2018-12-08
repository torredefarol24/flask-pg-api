from app import app, db
from app.models.User import User
from app.decorators.check_bearerToken import token_required
from flask import json, jsonify, request, Response
from app.helpers.error_funcs import invalid_request_method
from sqlalchemy.exc import IntegrityError, DataError, SQLAlchemyError, DBAPIError

import pprint

@app.route("/users", methods=['GET', 'POST'])
def users_Index():
  if request.method == 'GET':
    return get_all_users()
  elif request.method == 'POST':
    return register_user()
  else:
    return invalid_request_method()



@token_required
def get_all_users():
  users = User.query.order_by("id desc").all()
  context = {
    "success" : True,
    "message" : "Fetch All Users",
    "data" : []
  }
  for user in users:
    context['data'].append(user.toDict())
  response = jsonify(context)
  return response, 200



@token_required
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
    try :
      user.create()
      context["data"] = user.toDict()
    # except IntegrityError:
    #   context['data'] = None
    #   context['success'] = False
    #   context['message'] = "Email Taken"
    #   statusCode = 500
    # except DataError: 
    #   context['data'] = None
    #   context['success'] = False
    #   context['message'] = "Values Too Long"
    #   statusCode = 500
    except SQLAlchemyError as e:
      context['success'] = False
      context['message'] = str(e.__dict__['orig'])
      statusCode = 500

    return jsonify(context), statusCode
    