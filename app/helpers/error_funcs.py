from flask import jsonify

def invalid_request_method():
  context = {
    "success" : False,
    "data" : None,
    "message" : "Invalid Request Method"
  }
  return jsonify(error = context), 500