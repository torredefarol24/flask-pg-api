from app import flaskPgApp
import json

@flaskPgApp.route("/")
def index():
  context = {
    "message" : "Hey",
    "success" : True,
    "data" : []
  }
  return json.dumps(context)

@flaskPgApp.route("/hello/<name>")
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
  