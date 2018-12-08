from app import api
from app.models.User import User
from app.decorators.check_bearerToken import token_required
from flask_restful import Resource, reqparse


class User_List(Resource):
  def get(self):
    users = User.query.order_by("id desc").all()
    context = {
      "success" : True,
      "message" : "Fetch All Users",
      "data" : []
    }
    for user in users:
      context['data'].append( user.toDict() )
    
    return context

regDataParser = reqparse.RequestParser()
regDataParser.add_argument("fullname", type=str, help="Please Provide Fullname")
regDataParser.add_argument("email", type=str, help='Please Provide Email')
regDataParser.add_argument("password", type=str, help='Please Provide Password')


class User_Registration(Resource):
  def post(self):
    regData = regDataParser.parse_args()

    print(regData)
    return regData  


api.add_resource(User_List, "/users")
api.add_resource(User_Registration, "/users")