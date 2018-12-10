from app import app
from flask import request, json, Response
from app.decorators.check_bearerToken import token_required

@app.route("/")
def index():
  statusCode = int(200)
  context = {
    "message" : "Hey",
    "success" : True,
    "data" : [],
  }
  respData = json.dumps(context)
  response = Response(respData, status=statusCode)
  # return json.dumps(context), statusCode
  return response


@app.route("/hello/<string:name>")
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


@app.route("/dummy/search")
def dummySearch():
  statusCode = int(200)
  context = {
    "message" : "Req Args, Query Params",
    "success" : True,
    "data" : [
      {
        "query_params" : str(request.args['title'])[1:-1]
      }
    ]
  }
  return json.dumps(context), statusCode


@app.route("/dummy/protected/data")
@token_required
def sendProtectedData():
  statusCode = 200
  context = {
    "success" : True,
    "message" : "Token Requirement Decorator working",
    "data" : [
      {
        "id" : 1,
        "name" : "Dummy"
      },
      {
        "id" : 2,
        "name" : "Really"
      }
    ]
  }
  respData = json.dumps(context)
  response = Response(respData, status=statusCode)
  return response
  
