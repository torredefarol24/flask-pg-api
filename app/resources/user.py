from app import api
from app.models.User import User
from app.decorators.check_bearerToken import token_required
from flask_restful import Resource, reqparse
from flask import jsonify, json

class User_List(Resource):
  def get(self):
    users = User.find()
    context = {
      "success" : True,
      "message" : "Fetch All Users",
      "data" : json.dumps(users)
    }
    # for user in users:
    #   context['data'].append( user.toDict() )
    
    return jsonify(result=context)

class User_Registration(Resource):
  def post(self):
    regData = regDataParser.parse_args()

    print(regData)
    return regData  


api.add_resource(User_List, "/resources/users")
api.add_resource(User_Registration, "/resources/users")