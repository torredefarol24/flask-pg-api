from flask import jsonify

def invalid_request_method():
  context = {
    "success" : False,
    "data" : None,
    "message" : "Invalid Request Method"
  }
  return jsonify(error = context), 500

def invalid_request_headers():
  context = {
    "success" : False,
    "data" : None,
    "message" : "Invalid Request Headers"
  }
  return jsonify(error = context), 500