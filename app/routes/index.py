from app import flaskPgApp
from flask import request, json

@flaskPgApp.route("/")
def index():
  statusCode = int(200)
  context = {
    "message" : "Hey",
    "success" : True,
    "data" : [],
  }
  return json.dumps(context), statusCode

@flaskPgApp.route("/hello/<string:name>")
def sayHello(name):
  statusCode = int(200)
  context = {
    "message" : "route params",
    "data" : [
      {
        f'{name}' : name
      }
    ],
    "success" : True
  }
  return json.dumps(context), statusCode

@flaskPgApp.route("/dummy/search")
def dummySearch():
  statusCode = int(200)
  context = {
    "message" : "Req Args, Query Params",
    "success" : True,
    "data" : [
      {
        "query_params" : request.args['title']
      }
    ]
  }
  return json.dumps(context), statusCode

@flaskPgApp.route("/dummy/post/headers")
def dummyHeaders():
  statusCode = int(200)
  context = {
    "success" : True,
    "message" : "Request Headers Values"
  }
  
  if request.headers['Content-Type'] == 'text/plain':
    context["data"] = [
      {
        "text-data" : str(request.data)
      }
    ]
    return json.dumps(context), statusCode
  
  if request.headers['Content-Type'] == 'application/json':
    context["data"] = [
      {
        "json-data" : request.json
      }
    ]
    return json.dumps(context), statusCode
  
  if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
    context["data"] = [
      {
        "form-data-body" : {
          "num1" : request.form["num1"],
          "num3" : request.form["num3"]
        }
      }
    ]
    return json.dumps(context), statusCode
  else:
    context["data"] = []
    context["success"] = False
    context["message"] = "Content Type not processable"
    return json.dumps(context), statusCode


