from app import flaskPgApp
import json
from flask import request

@flaskPgApp.route("/")
def index():
  context = {
    "message" : "Hey",
    "success" : True,
    "data" : []
  }
  return json.dumps(context)

@flaskPgApp.route("/hello/<string:name>")
def sayHello(name):
  context = {
    "message" : "route params",
    "data" : [
      {
        f'{name}' : name
      }
    ],
    "success" : True
  }
  return json.dumps(context)

@flaskPgApp.route("/dummy/search")
def dummySearch():
  context = {
    "message" : "Req Args, Query Params",
    "success" : True,
    "data" : [
      {
        "query_params" : request.args['title']
      }
    ]
  }
  return json.dumps(context)

