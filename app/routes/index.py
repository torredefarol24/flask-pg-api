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
