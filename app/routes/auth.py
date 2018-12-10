from app import app
from flask_bcrypt import bcrypt
from app.models.User import User
from app.helpers.error_funcs import invalid_request_headers, invalid_request_method
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token, jwt_refresh_token_required



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


@app.route("/auth/token/refresh", methods=['POST'])
def authTokenRefresh():
  if not request.method == 'POST':
    return invalid_request_method()
  else:
    return refresh_user_token()



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
    token_data = {
      "user_id" : user.id,
      "user_email" : user.email
    }
    access_token = create_access_token(identity = token_data)
    refresh_token = create_refresh_token(identity = token_data)

    context['data'] = {
      "access_token" : access_token,
      "refresh_token" : refresh_token
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



@jwt_refresh_token_required
def refresh_user_token():
  token_content = get_jwt_identity()
  access_token = create_access_token(identity = token_content)
  context = {
    "success" : True,
    "message" : "Access Token Renewed",
    "access_token" : access_token
  }
  return jsonify(context), 200