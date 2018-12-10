from app import app
from flask_bcrypt import bcrypt
from app.models.User import User
from app.helpers.error_funcs import invalid_request_headers, invalid_request_method
from flask import request, jsonify


@app.route("/auth/login", methods=['POST'])
def authLogin():
  if not request.method == 'POST':
    return invalid_request_method()
  else:
    return authenticate_user()


@app.route("/auth/logout", methods=['GET'])
def authLogout():
  if not request.method == 'GET':
    return invalid_request_method()
  else:
    return logout_user()


def authenticate_user():
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Authenticating Users",
    "data" : {}
  }
  request_header_json = request.headers.get("Content-Type") == 'application/json'
  request_header_form = request.headers.get("Content-Type") == 'application/x-www-form-urlencoded'

  if request_header_json:
    user = User.findByEmail(request.json['email'])
    result = user.check_password(request.json['password'])

  elif request_header_form:
    user = User.findByEmail(request.form['email'])
    result = user.check_password(request.form['password'])
  else:
    return invalid_request_headers()
  
  if result:
    context['data'] = {
      "token" : 'IMAGINARY TOKEN'
    }
  else:
    context['success'] = False
    context['message'] = "Auth Failed"
    statusCode = 401
  return jsonify(context), statusCode


def logout_user():
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Logout User"
  }
  return jsonify(context), statusCode
